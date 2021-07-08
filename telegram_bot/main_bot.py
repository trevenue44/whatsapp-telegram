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
                          "\nA bot created to transfer messages from whatsapp to this telegram channel." + 
                          "\nAt your service." +
                          "\n\nType 'whatsapp' before every message that you want me to copy to Whatsapp.")


def whatsapp_request(message):
    # function returns true if message was intended to be sent to whatsapp.
    if message.text.split()[0].strip().lower() in ["whatsapp", "whatsapp."]:
        # if message starts with the whatsapp keyword
        return True
    else:
        return False

@bot.message_handler(func=whatsapp_request)
def send_to_whatsapp(message):
    hour = dt.datetime.now().hour
    minutes = dt.datetime.now().minute + 1
    print(hour, minutes)
    whatsap_message = message.text[9:].strip() # getting actual message content. excluding the 'whatsapp' command



bot.polling()
