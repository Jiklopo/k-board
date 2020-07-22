from rest_framework.views import APIView, Response
from telegram.bot import bot


class BotView(APIView):
    def post(self, request, format=None):
        print(request.data)
        bot.process_new_updates(request.data)
        return Response(status=200)
