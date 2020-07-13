from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class MessageView(TemplateView):
    template_name = 'message.html'
