from main.models import Add
from django import forms


class AddForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = ['title', 'description', 'category']
