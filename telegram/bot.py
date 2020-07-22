from k_board.settings import HEROKU_URL
import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
link = f'{HEROKU_URL}{TOKEN}'
webhook_info = bot.get_webhook_info()
if webhook_info.url == '' or webhook_info.url != link:
    bot.set_webhook(link)


def process_updates(json_data):
    bot.process_new_updates(telebot.types.Update.de_json(json_data))


@bot.message_handler(commands='week')
def test(message):
    bot.reply_to(message, 'Success!')
