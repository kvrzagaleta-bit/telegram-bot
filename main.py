import os
import telebot

# Get your bot token (for now directly in the script)
BOT_TOKEN = "8180984807:AAEK-Rwy_v-DItGqwxdyo0pcjpjJ7-WA5OpE"  # <-- replace with your token

bot = telebot.TeleBot(BOT_TOKEN)

# Basic start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello 👋, your bot is online and working!")

# Echo all messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
