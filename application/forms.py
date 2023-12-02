from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    # Определение пользовательской формы аутентификации
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'autofocus': True}))
    # Поле ввода логина с автофокусом
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # Поле ввода пароля с использованием виджета для пароля

class UserProfileForm(UserChangeForm):
    # Форма для изменения профиля пользователя
    password = None  # Исключаем поле пароля из формы

    class Meta:
        model = User  # Указываем модель пользователя
        fields = ('username', 'email', 'first_name', 'last_name')
        # Определяем поля, которые будут отображаться в форме

class UserRegisterForm(UserCreationForm):
    # Форма для регистрации нового пользователя
    email = forms.EmailField(required=True)  # Добавляем поле email как обязательное

    class Meta:
        model = User  # Указываем модель пользователя
        fields = ["username", "email", "password1", "password2"]
        # Определяем поля, которые будут включены в форму регистрации
