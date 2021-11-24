import telebot
import requests
from telebot import types

token = "2137785694:AAGT4E1TMEIxT8uWHGaYH8DoSfgZKIwrFsc"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/dawgs", "/echo", "/WebM")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я тупой бот, но кое-что умею')


@bot.message_handler(commands=['dawgs'])
def dawgs(message):
    bot.send_message(message.chat.id, 'Песики. Любишь песиков?')
    dawgs = requests.get('https://dog.ceo/api/breeds/image/random')
    bot.send_photo(message.chat.id, dawgs.json()['message'])


@bot.message_handler(commands=['/WebM'])
def WebM(message):
    bot.send_video(message.chat.id, "https://www.youtube.com/watch?v=D2jEM5aHHJc")


@bot.message_handler(commands=['/echo'])
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text == "/echo":
        global label
        bot.send_message(message.chat.id, 'Я повторю все, что ты скажешь')
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling()
