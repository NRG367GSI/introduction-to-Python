import telebot
from random import *
import json
from telebot import types
films=[]


def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")

def load():
    global films
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Фильмотека была успешно загружена")   


API_TOKEN='СЮДА ВСТАВЬТЕ ВАШ ТОКЕН ОТ BOTFATHER'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id,"Фильмотека была успешно загружена!")

    except:
        films.append("Матрица")
        films.append("Солярис")
        films.append("Властелин колец")
        films.append("Техасская резня бензопилой")
        films.append("Санта Барбара") 
        bot.send_message(message.chat.id,"Фильмотека была загружена по умолчанию!")


@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id,"Вот список фильмов")
    bot.send_message(message.chat.id, ", ".join(films))

@bot.message_handler(content_types='text')
def message_reply(message):
    if 'привет' in message.text :
        bot.send_message(message.chat.id,'и тебе привет')


bot.polling()