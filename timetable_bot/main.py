import datetime
import psycopg2
import telebot
from telebot import types

token = "2138524818:AAF1mpDhqDr8NGBwQVeFWI5LoqPXl8Bua1Y"
bot = telebot.TeleBot(token)
date = datetime.date.today().isocalendar()[1]

conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="root",
                        host="localhost",
                        port="5432")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Расписание на текущую неделю",
                 "Расписание на следующую неделю")
    bot.send_message(message.chat.id, 'Здесь можно посмотреть расписание БФИ2102', reply_markup=keyboard)


@bot.message_handler(commands=['week'])
def week(message):
    if date % 2 == 0:
        bot.send_message(message.chat.id, 'Сейчас нижняя неделя')
    if date % 2 == 1:
        bot.send_message(message.chat.id, 'Сейчас верхняя неделя')


@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '''Этот бот присылает расписание БФИ2102: по дням недели, на текущую и следующую неделю.
Бот автоматически определяет какая учебная неделя идет на данный момент.
    
/week - Текущая неделя
/help - Помощь
/mtuci - Ссылка на официальный сайт МТУСИ''')


@bot.message_handler(content_types=['text'])
def evenodd(message):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    final = []

    if message.text == "Понедельник" or message.text == "Вторник" or message.text == "Среда" or message.text == "Четверг" or message.text == "Пятница":
        day = message.text

        #нечетная
        if date % 2 == 1:
            result = []
            select_timetable = "SELECT day, subject, room_numb, start_time FROM service.timetable"
            timetable = execute_read_query(conn, select_timetable)
            for i in timetable:
                if i[0] == day:
                    for j in i:
                        if j == day:
                            continue
                        else:
                            result.append(str(j)+' ')
                    result.append('\n')
            bot.send_message(message.chat.id, '_____' + day + '_____' + '\n' + '\n' + ''.join(result))

        #четная
        if date % 2 == 0:
            result = []
            select_timetable = "SELECT day, subject, room_numb, start_time FROM service.timetable_even"
            timetable = execute_read_query(conn, select_timetable)
            for i in timetable:
                if i[0] == day:
                    for j in i:
                        if j == day:
                            continue
                        else:
                            result.append(str(j)+' ')
                    result.append('\n')
            bot.send_message(message.chat.id, '_____' + day + '_____' + '\n' + '\n' + ''.join(result))

    elif message.text == 'Расписание на текущую неделю':

        if date % 2 == 1:
            select_timetable = "SELECT day, subject, room_numb, start_time FROM service.timetable"
            timetable = execute_read_query(conn, select_timetable)
            for day in days:
                result = []
                for i in timetable:
                    if i[0] == day:
                        for j in i:
                            if j == day:
                                continue
                            else:
                                result.append(str(j)+' ')
                        result.append('\n')
                final.append('_____' + day + '_____' + '\n' + '\n' + ''.join(result) + '\n')
            bot.send_message(message.chat.id, ''.join(final))

        if date % 2 == 0:
            select_timetable = "SELECT day, subject, room_numb, start_time FROM service.timetable_even"
            timetable = execute_read_query(conn, select_timetable)
            for day in days:
                result = []
                for i in timetable:
                    if i[0] == day:
                        for j in i:
                            if j == day:
                                continue
                            else:
                                result.append(str(j) + ' ')
                        result.append('\n')
                if day == 'Четверг':
                    result.append('Нет пар, гуляем')
                    result.append('\n')
                final.append('_____' + day + '_____' + '\n' + '\n' + ''.join(result) + '\n')
            bot.send_message(message.chat.id, ''.join(final))

    elif message.text == 'Расписание на следующую неделю':

        if date % 2 == 0:
            select_timetable = "SELECT day, subject, room_numb, start_time FROM service.timetable"
            timetable = execute_read_query(conn, select_timetable)
            for day in days:
                result = []
                for i in timetable:
                    if i[0] == day:
                        for j in i:
                            if j == day:
                                continue
                            else:
                                result.append(str(j) + ' ')
                        result.append('\n')
                final.append('_____' + day + '_____' + '\n' + '\n' + ''.join(result) + '\n')
            bot.send_message(message.chat.id, ''.join(final))

        if date % 2 == 1:
            select_timetable = "SELECT day, subject, room_numb, start_time FROM service.timetable_even"
            timetable = execute_read_query(conn, select_timetable)
            for day in days:
                result = []
                for i in timetable:
                    if i[0] == day:
                        for j in i:
                            if j == day:
                                continue
                            else:
                                result.append(str(j) + ' ')
                        result.append('\n')
                if day == 'Четверг':
                    result.append('Нет пар, гуляем!')
                    result.append('\n')
                final.append('_____' + day + '_____' + '\n' + '\n' + ''.join(result) + '\n')
            bot.send_message(message.chat.id, ''.join(final))

    else:
        bot.send_message(message.chat.id, 'Я Вас не понял. Повторите запрос.')


bot.polling()
