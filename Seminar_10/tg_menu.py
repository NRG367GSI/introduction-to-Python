import telebot
from telebot import types
import controller as cr
import working_with_database as wwd

API_TOKEN = '5426760478:AAFaaDf7G9X421DPaqCNwuTWmwN_tA_xm1E'
bot = telebot.TeleBot(API_TOKEN)
record = {}


@bot.message_handler(commands=['start'])
def start_message(message):
  mess = f' Информационная система запущена\n' \
         f'⬇️В левом нижнем углу ты можешь воспользоваться меню↙️'
  bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['add'])
def add_cmd(message):
  msg = bot.send_message(message.chat.id,
                         'Введите имя и фамилию ученика⬇️')
  bot.register_next_step_handler(msg, name_step)


def name_step(message):
  global record
  record['name'] = message.text
  msg = bot.send_message(message.chat.id, 'Введите дату рождения⬇️')
  bot.register_next_step_handler(msg, birthday_step)


def birthday_step(message):
  global record
  record['hb'] = message.text
  msg = bot.send_message(message.chat.id,
                         'Введите номер класса⬇️')
  bot.register_next_step_handler(msg, class_step)


def class_step(message):
  global record
  record['class'] = message.text
  msg = bot.send_message(message.chat.id,
                         'Введите успеваемость⬇️')
  bot.register_next_step_handler(msg, status_step)


def status_step(message):
  global record
  record['status'] = message.text
  wwd.add_in_file(record)
  bot.send_message(message.chat.id, 'Запись успешно добавлена!✅')


@bot.message_handler(commands=['delete'])
def delete(message):
  msg = bot.send_message(message.chat.id,
                         'Напишите фамилию и имя ученика которого хотите удалить из списка 🗑')
  bot.register_next_step_handler(msg, deleting_data_in_db_step)


def deleting_data_in_db_step(message):
  wwd.deleting(message.text)
  bot.send_message(message.chat.id, 'Запись успешно удалена!✅')



@bot.message_handler(commands=['view'])
def view(message):
  cr.list_file()
  bot.send_message(message.chat.id, cr.list_file())

@bot.message_handler(commands=['add'])
def add(message):
    
    bot.send_message(message.chat.id, cr.add_record())


@bot.message_handler(commands=['search'])
def search(message):
  key = types.InlineKeyboardMarkup()
  but_1 = types.InlineKeyboardButton(text="Поиск по фамилии и имени",
                                     callback_data="NumberOne")
  but_2 = types.InlineKeyboardButton(text="Поиск по дате рождения",
                                     callback_data="NumberTwo")
  but_3 = types.InlineKeyboardButton(text="Поиск по классам",
                                     callback_data="NumberTree")
  but_4 = types.InlineKeyboardButton(text="Поиск по успеваймости",
                                     callback_data="NumberFour")
  key.add(but_1, but_2, but_3, but_4)
  bot.send_message(message.chat.id, "Выбирите интерисующий пункт меню",
                   reply_markup=key)


@bot.callback_query_handler(func=lambda c:True) # тут надо будет посмотреть чтоб в меседже методы из контролера возращали текст
def inline(c):
  if c.data == 'NumberOne':
    bot.send_message(c.message.chat.id, cr.name_search())
  if c.data == 'NumberTwo':
    bot.send_message(c.message.chat.id, cr.birthdey_search())
  if c.data == 'NumberTree':
    bot.send_message(c.message.chat.id, cr.grade_search())
  if c.data == 'NumberFour':
    bot.send_message(c.message.chat.id, cr.performance_serch())


bot.polling()
