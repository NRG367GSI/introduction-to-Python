import telebot
from telebot import types

API_TOKEN='5796391696:AAGSvDEM13e-8cIgX07oZKQ3JKADFw_ekzU'
bot = telebot.TeleBot(API_TOKEN)

#srart 
#@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'It works!') #Выводит сообщение


#открывает изображение и после нажатия старта в чате отпровляет изображение и сообщение
img = open('shem.jpg', 'rb')
#@bot.message_handler(commands=['start'])
def start(message):
	bot.send_photo(message.chat.id, photo=img, caption='It works!')




# после старта добовляет кнобки
#@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup()
  buttonA = types.KeyboardButton('A')
  buttonB = types.KeyboardButton('B')
  buttonC = types.KeyboardButton('C')
  markup.row(buttonA, buttonB)
  markup.row(buttonC)
  bot.send_message(message.chat.id, 'It works!', reply_markup=markup)

'''
ReplyKeyboardMarkup – и есть та самая клавиатура. Метод row() создает ряд (максимум 12) из кнопок, передаваемых в качестве аргумента.
Также есть особенная клавиатура types.ReplyMarkupRemove(), которая меняет клавиатуру на стандартную.
'''

bot.polling()