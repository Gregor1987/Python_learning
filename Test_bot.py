import telebot
import parser

token = ''
bot = telebot.TeleBot(token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Погода')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Тюмень', 'Пермь')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Погода':
        bot.send_message(message.chat.id, 'Где?', reply_markup=keyboard2)
    if message.text == 'Тюмень':
        bot.send_message(message.chat.id, parser.weather_tyumen())
    if message.text == 'Пермь':
        bot.send_message(message.chat.id, parser.weather_perm())


bot.polling()
