from django.forms import ModelForm
from django.forms.widgets import PasswordInput
from .models import User
from django import forms


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            ]

        widgets = {
            "password1":PasswordInput(),
            "password2":PasswordInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=PasswordInput())