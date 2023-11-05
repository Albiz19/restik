from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser


class UserProfileForm(UserChangeForm):
    password = None  # Исключаем поле пароля из формы

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')