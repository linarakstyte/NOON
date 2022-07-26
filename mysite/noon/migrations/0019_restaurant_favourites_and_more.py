# Generated by Django 4.0.6 on 2022-07-19 08:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noon', '0018_remove_restaurant_reader'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='dessert',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Dessert'),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='first_main',
            field=models.CharField(blank=True, default='main', max_length=200, verbose_name='First Main'),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='second_main',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Second Main'),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='soup',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Soup'),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='third_main',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Third Main'),
        ),
    ]
