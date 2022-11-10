import telebot
from telebot import types
import controller as cr
import working_with_database as wwd
import search_data as sd

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
                         'Введите успеваемость ("отл","хор" или "удв")⬇️')
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


@bot.message_handler(commands=['search'])
def search(message):
  key = types.InlineKeyboardMarkup()
  but_1 = types.InlineKeyboardButton(text="По фамилии и имени",
                                     callback_data="NumberOne")
  but_2 = types.InlineKeyboardButton(text="По дате рождения",
                                     callback_data="NumberTwo")
  but_3 = types.InlineKeyboardButton(text="По классам",
                                     callback_data="NumberTree")
  but_4 = types.InlineKeyboardButton(text="По успеваймости",
                                     callback_data="NumberFour")
  key.add(but_1, but_2, but_3, but_4)
  bot.send_message(message.chat.id, "Выбирите критерий поиска",
                   reply_markup=key)

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
  if c.data == 'NumberOne':
    msg = bot.send_message(c.message.chat.id, 'Напишите фамилию и имя ученика которого хотите')
    bot.register_next_step_handler(msg, search_name_step)
  if c.data == 'NumberTwo':
    msg = bot.send_message(c.message.chat.id, 'Введите дату рождения по которой по которой хотите начать поиск')
    bot.register_next_step_handler(msg, search_birthday_step)
  if c.data == 'NumberTree':
    msg = bot.send_message(c.message.chat.id, 'Введите номер класса по которому хотите просмотреть информацию')
    bot.register_next_step_handler(msg, search_class_step)
  if c.data == 'NumberFour':
    msg = bot.send_message(c.message.chat.id, 'Введите статус успеваемости')
    bot.register_next_step_handler(msg, search_status_step)

def search_name_step(message):
  msg = sd.search_name_in_db(message.text)
  bot.send_message(message.chat.id, msg)

def search_birthday_step(message):
  msg = sd.search_birthday_in_db(message.text)
  bot.send_message(message.chat.id, msg)

def search_class_step(message):
  msg = sd.search_class_in_db(message.text)
  bot.send_message(message.chat.id, msg)

def search_status_step(message):
  msg = sd.search_status_in_db(message.text)
  bot.send_message(message.chat.id, msg)


bot.polling()
