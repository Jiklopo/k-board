from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView


class LoginView(views.LoginView):
    pass


class LogoutView(views.LogoutView):
    redirect_field_name = '/'


class RegistrationView(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/'


class ProfileView(LoginRequiredMixin, TemplateView):
    pass
