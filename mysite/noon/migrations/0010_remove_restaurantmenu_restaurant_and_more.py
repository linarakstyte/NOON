# Generated by Django 4.0.6 on 2022-07-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noon', '0009_restaurantmenu_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantmenu',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='restaurantmenu',
            name='dish',
        ),
        migrations.AddField(
            model_name='restaurantmenu',
            name='dish',
            field=models.ManyToManyField(related_name='restaurant', to='noon.restaurant'),
        ),
    ]
