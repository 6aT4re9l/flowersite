# Generated by Django 4.2.10 on 2024-03-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0002_alter_products_options_products_visibility_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="discount",
            field=models.IntegerField(default=0, verbose_name="Скидка в процентах"),
        ),
        migrations.AlterField(
            model_name="products",
            name="name",
            field=models.CharField(
                max_length=150, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="price",
            field=models.IntegerField(default=0, verbose_name="Цена"),
        ),
        migrations.AlterField(
            model_name="products",
            name="quantity",
            field=models.PositiveIntegerField(default=0, verbose_name="Количество"),
        ),
        migrations.AlterField(
            model_name="products",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=200, null=True, unique=True, verbose_name="URL"
            ),
        ),
    ]
