# Generated by Django 4.2.6 on 2023-11-26 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0004_alter_cart_options_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
    ]
