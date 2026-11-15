import telebotimport logging
logging.basicConfig(level=logging.INFO)
TOKEN = '9268543155:AAEhBueUiVx44CrPpxw6uXlxGbKHT3Reao'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
bot.reply_to(message, "হ্যালো! আমি আপনার বোট। কীভাবে সাহায্য করতে পারি?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
bot.reply_to(message, message.text)
if name == 'main':
logging.info("Bot is running...")
bot.infinity_polling()
