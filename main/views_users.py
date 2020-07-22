from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from main.forms import *


class LoginView(views.LoginView):
    template_name = 'users/form.html'


class LogoutView(LoginRequiredMixin, views.LogoutView):
    template_name = 'index.html'
    redirect_field_name = '/'


class ChangePasswordView(LoginRequiredMixin, views.PasswordChangeView):
    template_name = 'users/form.html'

    def get_success_url(self):
        return reverse('main:message') + '?message=Password_Changed'


class RegistrationView(generic.CreateView):
    template_name = 'users/form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main:profile')

    def form_valid(self, form):
        user = form.save()
        user_info = UserInfo.objects.create(user_id=user.id)
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        adds = Add.objects.filter(user_id=self.request.user.id)
        return {'adds': adds}


class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'users/profile_edit.html'
    form_class = UserInfoForm
    success_url = reverse_lazy('main:profile')

    def get_object(self, queryset=None):
        try:
            user_info = UserInfo.objects.get(user_id=self.request.user.id)
        except UserInfo.DoesNotExist:
            user_info = UserInfo.objects.create(user_id=self.request.user.id)
        return user_info
