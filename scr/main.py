#import logging

from datetime import datetime

import config
import telebot
from telebot import types

TOKEN = "5762860883:AAEJnphqIYh7H6gYlsRUK3U_dbgte6Iiyfw"

bot=telebot.TeleBot(TOKEN)

current_datetime = datetime.now()

###################################
#############КОМАНДЫ123###############
###################################
@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Не знаю с чего начать')
    btn2 = types.KeyboardButton('Выбор сотового оператора')
    btn3 = types.KeyboardButton('Оформление медицинской страховки')
    btn4 = types.KeyboardButton('Получить Турецкий ИНН')
    btn5 = types.KeyboardButton('Документы для ВНЖ')
    btn6 = types.KeyboardButton('Как открыть счет в банке')
    btn7 = types.KeyboardButton('Сервисы по доставке')
    btn8 = types.KeyboardButton('Ремонт компьютеров')
    btn9 = types.KeyboardButton('Telegram канал')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    final_message = "Выбери интересующий тебя пункт (command)"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHL9ZjvDF5IxilLU609FY9QkYTfEmZ8AACFQADDhZaFHrF8ATYZDJYLQQ')
    bot.send_message(message.chat.id, current_datetime)

@bot.message_handler(commands=['test'])
def help(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHL9ZjvDF5IxilLU609FY9QkYTfEmZ8AACFQADDhZaFHrF8ATYZDJYLQQ')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Не знаю с чего начать')
    btn2 = types.KeyboardButton('Выбор сотового оператора')
    btn3 = types.KeyboardButton('Оформление медицинской страховки')
    btn4 = types.KeyboardButton('Получить Турецкий ИНН')
    btn5 = types.KeyboardButton('Документы для ВНЖ')
    btn6 = types.KeyboardButton('Как открыть счет в банке')
    btn7 = types.KeyboardButton('Сервисы по доставке')
    btn8 = types.KeyboardButton('Ремонт компьютеров')
    btn9 = types.KeyboardButton('Telegram канал')
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
    greetings = f'Привет!, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, greetings, parse_mode='html', reply_markup=markup)

###################################
#############КОМАНДЫ###############
###################################

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "не знаю с чего начать":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Вы находитесь на территории Турции')
        btn2 = types.KeyboardButton('Вы за пределами Турции')
        btn3 = types.KeyboardButton('В меню')
        markup.add(btn1, btn2, btn3)
        final_message = "Выбери один из вариантов ниже:"
        bot.send_message(message.chat.id, final_message, reply_markup=markup)

    elif get_message_bot == "вы находитесь на территории турции":
        final_message = 'Едь в Казахстан'
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    elif get_message_bot == "вы за пределами турции":
        final_message = 'Может, <b>Армения?</b>'
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    elif get_message_bot == "выбор сотового оператора":
        # sendPhoto
        #photo = open('/scr/bot/img/folder.png', 'rb')
        final_message = 'Однозначно, Turkсell.\nСтоимость туристического тарифа не более 550 Tl (включает 20GB).\n<b>Через 90 дней блокируются интернет, исходящие звонки и смс (работает только прием звонков и смс)</b>\nРазблокировка возможна <b>ТОЛЬКО</b> после получения ВНЖ.'
        bot.send_message(message.chat.id, final_message, parse_mode='html')
        #bot.send_photo(chat_id, photo)
        #bot.send_photo(chat_id, "FILEID")

    elif get_message_bot == "оформление медицинской страховки":
        markup = types.InlineKeyboardMarkup()
        final_message = "тут про страховку"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "получить турецкий инн":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Заполни анкету для получения ИНН", url="https://ivd.gib.gov.tr/"))
        final_message = "Жми на APPLICATION FOR NON-CITIZEN'S POTENTIAL TAX NUMBER"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "документы для внж":
        markup = types.InlineKeyboardMarkup()
        final_message = "список документов для внж: 1)....\n2)...\n3)"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "как открыть счет в банке":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Жми", url="https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD"))
        final_message = "Едь в Казахстан"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "сервисы по доставке":
        markup = types.InlineKeyboardMarkup()
        final_message = "сервисы по доставке: 1)....\n2)...\n3)"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "ремонт компьютеров":
        markup = types.InlineKeyboardMarkup()
        final_message = "ремонт компьютеров: 1)....\n2)...\n3@!"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "telegram канал":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на канал", url="https://t.me/russiansinturkey_antalya"))
        final_message = "Переходи по ссылке"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Не знаю с чего начать')
        btn2 = types.KeyboardButton('Выбор сотового оператора')
        btn3 = types.KeyboardButton('Оформление медицинской страховки')
        btn4 = types.KeyboardButton('Получить Турецкий ИНН')
        btn5 = types.KeyboardButton('Документы для ВНЖ')
        btn6 = types.KeyboardButton('Как открыть счет в банке')
        btn7 = types.KeyboardButton('Сервисы по доставке')
        btn8 = types.KeyboardButton('Ремонт компьютеров')
        btn9 = types.KeyboardButton('Telegram канал')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        final_message = "Выбери интересующий тебя пункт (else)"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)