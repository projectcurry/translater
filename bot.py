import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from logic import *

bot = telebot.TeleBot("8186123141:AAForIZo2wl0p2f6Z1N-rKXq-MJtBjTQpKc")

def gen_markup_for_text():
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton('Получить ответ', callback_data='text_ans'),
                   InlineKeyboardButton('Перевести сообщение', callback_data='text_translate'))
        
        return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if "text" in call.data:
        obj = TextAnalysis.memory[call.from_user.username][-1]
        if call.data == "text_ans":
            bot.send_message(call.message.chat.id, obj.response)
        elif call.data == "text_translate":
            bot.send_message(call.message.chat.id,  obj.translation)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Дополнительное задание
    TextAnalysis(message.text, message.from_user.username)
    bot.send_message(message.chat.id, "Я получил твое сообщение! Что ты хочешь с ним сделать?", reply_markup=gen_markup_for_text())

bot.infinity_polling(none_stop=True)
