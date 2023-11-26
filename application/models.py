from profile import Profile

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
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


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    email = models.CharField(max_length=15, blank=True, null=True, verbose_name='Почта')
    birth_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Фамилия')

    # Add related_name in groups and user_permissions to avoid clash
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",
        related_query_name="customuser",
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",
        related_query_name="customuser",
        verbose_name='user permissions',
    )

    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_or_update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #     instance.profile.save()


class RestaurantInfo(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название ресторана')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    location = models.TextField(verbose_name='Расположение')  # может быть полем для геоданных

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Информация о ресторане'
        verbose_name_plural = 'Информация о ресторанах'


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Favorite(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='Товар'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']

    def __str__(self):
        return self.title
