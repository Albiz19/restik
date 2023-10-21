from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название ресторана')
    description = models.TextField(verbose_name='Описание ресторана',blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес',blank=True)
    phone_number = models.CharField(max_length=15, verbose_name='Телефон',blank=True)
    email = models.EmailField(verbose_name='Email',blank=True)
    website = models.URLField(verbose_name='Веб-сайт',blank=True)
    image = models.ImageField(upload_to='restaurant_images/', verbose_name='Изображение ресторана',blank=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=255, verbose_name='Название блюда')
    description = models.TextField(verbose_name='Описание блюда')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name
