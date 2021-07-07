import telebot
import os
from dotenv import load_dotenv
load_dotenv() # using env variables to protect the API_KEY

API_KEY = os.environ.get('API_KEY')

bot = telebot.TeleBot(API_KEY) # creating the bot

@bot.message_handler(commands=["start"]) # looking out for the start message
def start(message):
    # initial message when the bought is activated
    bot.reply_to(message, "Hello.\nWhat's up?" + 
                          "\nA bot created to transfer messages from whatsapp to this telegram channel." + 
                          "\nAt your service." +
                          "\nType '/whatsapp' to get the latest messgaes")

@bot.message_handler(commands=["whatsapp"])
def whatsapp(message):
    # sends messages from whatsapp when the /whatsapp commmand is issued
    bot.reply_to(message, "Can't access whatsapp now.") 
    # "Can't access whatsapp now" will be changed to an actual message when we can access whatsapp messages



bot.polling()
