# Generated by Django 4.2.6 on 2023-12-08 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0002_alter_cart_user_alter_favorite_user_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="RestaurantInfo",),
    ]