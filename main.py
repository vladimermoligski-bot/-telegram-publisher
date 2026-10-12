import os
import telebot

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("Не задан TELEGRAM_BOT_TOKEN в настройках облака")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет! Бот работает! 🚀")

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(message, "Бот запущен и готов к настройке публикаций!")

bot.infinity_polling()
