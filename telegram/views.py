from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import Response
from telegram.bot import bot


@csrf_exempt
def telegram_webhook(request):
    print(request.data)
    bot.process_new_updates(request.data)
    return Response(status=200)
