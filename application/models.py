from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Делаем поле email обязательным
    first_name = forms.CharField(max_length=30, required=True)  # Делаем поле first_name обязательным
    last_name = forms.CharField(max_length=30, required=True)  # Делаем поле last_name обязательным

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class Category(models.Model):
    # Модель категории товаров
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    # Модель товара
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=150, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Фотография')
    on_sale = models.BooleanField(default=False, verbose_name='По акции')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class RestaurantInfo(models.Model):
    # Модель с информацией о ресторане
    name = models.CharField(max_length=150, verbose_name='Название ресторана')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    location = models.TextField(verbose_name='Расположение')  # Может быть полем для геоданных

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Информация о ресторане'
        verbose_name_plural = 'Информация о ресторанах'


class Cart(models.Model):
    # Модель корзины пользователя
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Favorite(models.Model):
    # Модель избранных товаров пользователя
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    timestamp = models.DateTimeField(auto_now_add=True)  # Время добавления товара в избранное

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        unique_together = ('user', 'product')  # Уникальность пары пользователь-товар


class News(models.Model):
    # Модель новостей ресторана
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']  # Сортировка новостей по убыванию даты публикации

    def __str__(self):
        return self.title
