import telebot
from telebot import types
import calc_complex_numbers as complex
import calc_rational_numbers as rational

bot = telebot.TeleBot('5796391696:AAGSvDEM13e-8cIgX07oZKQ3JKADFw_ekzU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать!")

@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Калькулятор Рациональных чисел', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Калькулятор комплексных чисел', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Крестики нолики', callback_data=5))
    bot.send_message(message.chat.id, text="Выберете, интерисующую функцию: ", reply_markup=markup)


@bot.message_handler(commands=["start","Hello"])
def start(message):
    msg = bot.send_message(message.chat.id, 'привет, введи любой текст и отправь')
    bot.register_next_step_handler(msg, start_2)


def start_2(message):
    bot.send_message(message.chat.id, 'на предыдущем шаге вы ввели\n{}'.format(message.text))


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Функция запущена!')
    answer = ''
    if call.data == '3':
        answer = 'Вы троечник!'
    elif call.data == '4':
        answer = 'Вы хорошист!'
    elif call.data == '5':
        answer = 'Вы отличник!'
    bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть