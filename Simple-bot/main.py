import telebot
import requests
from telebot import types


token = "2137785694:AAGT4E1TMEIxT8uWHGaYH8DoSfgZKIwrFsc"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/dawgs", "/webm", "/joke")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '''Здесь не так много функций, но:
    
"Хочу" - ссылка на паблик МТУСИ
/help - список функций бота
/dawgs - рандомный песик
/webm - видео из личного видеоархива
/joke - несмешная шутка про Чака Норриса на языке белых людей
''')


@bot.message_handler(commands=['dawgs'])
def dawgs(message):
    bot.send_message(message.chat.id, 'Песики. Любишь песиков?')
    dawgs = requests.get('https://dog.ceo/api/breeds/image/random')
    bot.send_photo(message.chat.id, dawgs.json()['message'])


@bot.message_handler(commands=['webm'])
def WebM(message):
    webm = open("b.mp4", "rb")
    bot.send_video(message.chat.id, webm)


@bot.message_handler(commands=['joke'])
def joke(message):
    jokes = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
    bot.send_message(message.chat.id, jokes.json()['joke'])


@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')

    elif message.text.lower() == "сигареты есть?":
        bot.send_message(message.chat.id, 'имеются')

    elif message.text.lower() == "а выпить есть?":
        bot.send_message(message.chat.id, 'а выпить нет')

    elif message.text.lower() == "ну на нет и суда нет":
        bot.send_message(message.chat.id, ':(')

    else:
        bot.send_message(message.chat.id, message.text)


bot.polling()
