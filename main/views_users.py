from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class LoginView(views.LoginView):
    redirect_field_name = ''
    redirect_authenticated_user = True


class LogoutView(views.LogoutView):
    redirect_field_name = ''
    redirect_authenticated_user = True


class RegistrationView(generic.CreateView):
    form_class = UserCreationForm
    success_url = ''
