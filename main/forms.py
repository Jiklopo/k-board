from main.models import Add, UserInfo
from django import forms


class AddForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = ['title', 'description', 'category']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['birth_date', 'admission_year', 'faculty']
