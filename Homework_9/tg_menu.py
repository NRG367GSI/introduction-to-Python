import telebot
from telebot import types

bot = telebot.TeleBot('5796391696:AAGSvDEM13e-8cIgX07oZKQ3JKADFw_ekzU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать!")

@bot.add_callback_query_handler
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть