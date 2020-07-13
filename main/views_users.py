from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView


class LoginView(views.LoginView):
    template_name = 'users/form.html'


class LogoutView(views.LogoutView):
    template_name = 'index.html'
    redirect_field_name = '/'


class ChangePasswordView(views.PasswordChangeView):
    template_name = 'users/form.html'


class RegistrationView(generic.CreateView):
    template_name = 'users/form.html'
    form_class = UserCreationForm
    success_url = '/'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
