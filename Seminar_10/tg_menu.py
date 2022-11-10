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
def start_message(message):
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


# после старта добовляет кнобки
# @bot.message_handler(commands=['start'])
# def start(message):
#   markup = types.ReplyKeyboardMarkup()
#   buttonA = types.KeyboardButton('A')
#   buttonB = types.KeyboardButton('B')
#   buttonC = types.KeyboardButton('C')
#   markup.row(buttonA, buttonB)
#   markup.row(buttonC)
#   bot.send_message(message.chat.id, 'It works!', reply_markup=markup)
bot.polling()
