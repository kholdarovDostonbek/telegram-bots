from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '7555346058:AAGDG6F2z5qYHFGu2tpzC3tiYJ8wjEXH2fI'

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Hello, Welcome!. \n Enter the your text: "
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message:True)
def echo_text(message):
    msg = message.text

    if msg.isascii(): 
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob )

bot.polling()

 
