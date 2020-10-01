from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import Response
from telegram.bot import bot
from telebot.types import Update


@csrf_exempt
@api_view(['POST'])
def telegram_webhook(request):
    print(request.data)
    update = Update.de_json(request.data)
    bot.process_new_updates([update])
    return Response(status=200)
