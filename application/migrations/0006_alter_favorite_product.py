# Generated by Django 4.2.6 on 2023-11-26 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0005_alter_product_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favorite",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="application.product",
                verbose_name="Товар",
            ),
        ),
    ]
