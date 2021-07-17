import datetime as dt
from utils import telegram_bot
my_bot = telegram_bot.main_bot.bot

def whatsapp_request(message):
    # function returns true if message was intended to be sent to whatsapp.
    if message.text.split()[0].strip().lower() in ["whatsapp", "whatsapp."]:
        # if message starts with the whatsapp keyword
        return True
    else:
        return False

@my_bot.message_handler(func=whatsapp_request)
def send_whatsapp_message(message):
    hour = dt.datetime.now().hour
    minutes = dt.datetime.now().minute
    telegram_msg = message.text[9:].strip() + f"\nTime Sent: {hour}:{minutes}"# getting actual message content. excluding the 'whatsapp' command
    my_bot.reply_to(message, "Received Successfully!")
    print(telegram_msg)

telegram_bot.start_polling()
