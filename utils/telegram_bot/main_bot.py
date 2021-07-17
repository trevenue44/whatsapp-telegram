import telebot
import os
from dotenv import load_dotenv
import datetime as dt
load_dotenv() # using env variables to protect the API_KEY

API_KEY = os.environ.get('API_KEY')

bot = telebot.TeleBot(API_KEY) # creating the bot

@bot.message_handler(commands=["start"]) # looking out for the start message
def start(message):
    # initial message when the bought is activated
    bot.reply_to(message, "Hello.\nWhat's up?" + 
                          "\nA bot created to transfer messages from this telegram channel to whatsapp." + 
                          "\nAt your service." +
                          "\n\nType 'whatsapp' before every message that you want me to copy to Whatsapp.")

def start_polling():
    bot.polling()
