# Generated by Django 4.0.6 on 2022-07-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noon', '0005_remove_restaurantmenu_restaurant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmenu',
            name='dish',
            field=models.ManyToManyField(related_name='restaurant', to='noon.restaurant'),
        ),
    ]