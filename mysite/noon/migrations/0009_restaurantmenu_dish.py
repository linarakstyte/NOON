# Generated by Django 4.0.6 on 2022-07-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noon', '0008_remove_restaurantmenu_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantmenu',
            name='dish',
            field=models.CharField(default='dish of the day', max_length=200, verbose_name='Dish'),
        ),
    ]
