from django.urls import path
from telegram import views
import os

app_name = 'telegram'
urlpatterns = [
    path(os.getenv('BOT_TOKEN'), views.telegram_webhook, name='bot_webhook')
]
