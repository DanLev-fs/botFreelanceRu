import telebot
import parse

parse.auth()

bot = telebot.TeleBot('');

keyboard = telebot.types.ReplyKeyboardMarkup(True)
markup = telebot.types.InlineKeyboardMarkup(row_width=3)

key = telebot.types.InlineKeyboardButton(text='Up', callback_data='pra')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

keyboard.row("Обновить")

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text == 'Обновить':
		for i in parse.parse():
			r = i[0] + "\n\n" + i[1] + "\n" + i[2]
			bot.send_message(message.chat.id, r)
		
bot.polling()
