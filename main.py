import telebot
import logging

logging.basicConfig(level=logging.INFO)
TOKEN = '9268543155:AAEHBueUivX44CrPxpwx6uXlxGbKHT3Reao'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "হ্যালো! আমি আপনার বট। কীভাবে সাহায্য করতে পারি?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
if __name__ == '__main__':
    logging.info("Bot is running...
bot.infinity_polling()
