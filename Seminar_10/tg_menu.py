import telebot
from telebot import types
import controller as cr

API_TOKEN='5796391696:AAGSvDEM13e-8cIgX07oZKQ3JKADFw_ekzU'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Это информационная система, для контроля успеваймости!') #Выводит сообщение

'''
В меню кнобки
menu = ["Список всех учеников", "Поиск с опцыямя", "Добавить запись", "Просмотр истории", "Удалить Запись"]
'''

@bot.message_handler(commands=['view'])
def view(message):
    cr.list_file()
    bot.send_message(message.chat.id, cr.list_file())



# после старта добовляет кнобки
@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup()
  buttonA = types.KeyboardButton('A')
  buttonB = types.KeyboardButton('B')
  buttonC = types.KeyboardButton('C')
  markup.row(buttonA, buttonB)
  markup.row(buttonC)
  bot.send_message(message.chat.id, 'It works!', reply_markup=markup)

bot.polling()