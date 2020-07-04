from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views import generic


class LoginView(views.LoginView):
    pass


class LogoutView(views.LogoutView):
    pass


class RegistrationView(generic.CreateView):
    form_class = UserCreationForm
    success_url = ''
