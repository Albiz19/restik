# Generated by Django 4.1.2 on 2023-10-21 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название ресторана"),
                ),
                ("description", models.TextField(verbose_name="Описание ресторана")),
                ("address", models.CharField(max_length=255, verbose_name="Адрес")),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Телефон"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("website", models.URLField(verbose_name="Веб-сайт")),
                (
                    "image",
                    models.ImageField(
                        upload_to="restaurant_images/",
                        verbose_name="Изображение ресторана",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название блюда"),
                ),
                ("description", models.TextField(verbose_name="Описание блюда")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена"
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menu_items",
                        to="application.restaurant",
                    ),
                ),
            ],
        ),
    ]
