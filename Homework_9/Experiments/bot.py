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
@bot.message_handler(commands=['start'])
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

# URL-кнопки, их цель - просто перекидывать пользователей по определенным веб-адресам
@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


#bot.polling()

# Обычный режим
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


# Инлайн-режим с непустым запросом
@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    # Добавляем колбэк-кнопку с содержимым "test"
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
    results = []
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)


# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")

if __name__ == '__main__':
    bot.infinity_polling()