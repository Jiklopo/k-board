from django.urls import path
from telegram import views
import os

app_name = 'telegram'
urlpatterns = [
    path(os.getenv('BOT_TOKEN'), views.BotView.as_view(), name='bot_webhook')
]
