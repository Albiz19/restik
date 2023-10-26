from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    @property
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=150, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Фотография')
    on_sale = models.BooleanField(default=False, verbose_name='По акции')

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')

    # Если вы используете свои связи ManyToMany, добавьте related_name
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="customuser",
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="customuser",
        verbose_name='user permissions',
    )


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок новости')
    content = models.TextField(verbose_name='Содержание')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title


class RestaurantInfo(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название ресторана')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    location = models.TextField(verbose_name='Расположение')  # может быть полем для геоданных

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites',
                             verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
