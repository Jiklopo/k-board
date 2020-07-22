import time

from k_board.settings import HEROKU_URL
import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN, threaded=False)
link = f'{HEROKU_URL}{TOKEN}'
webhook_info = bot.get_webhook_info()
print(f'webhook url "{webhook_info.url}"')
if webhook_info.url == '' or webhook_info.url != link:
    bot.remove_webhook()
    time.sleep(.1)
    bot.set_webhook(link)
    print(f'Set webhook url to "{link}"')


@bot.message_handler(content_types=['text'])
def test(message):
    print(message.text)
    bot.reply_to(message, message.text)


def process_updates(json_data):
    bot.process_new_updates([telebot.types.Update(**json_data)])
