# Generated by Django 4.0.6 on 2022-07-09 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noon', '0012_restaurantweeklymenu_remove_weeklymenu_weekday_menu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='dessert',
            field=models.CharField(blank=True, help_text='optional', max_length=200, null=True, verbose_name='Dessert'),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='first_main',
            field=models.CharField(blank=True, default='dish of the day', max_length=200, verbose_name='First Main'),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant', to='noon.restaurant', verbose_name='Restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='second_main',
            field=models.CharField(blank=True, help_text='optional', max_length=200, null=True, verbose_name='Second Main'),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='soup',
            field=models.CharField(blank=True, help_text='optional', max_length=200, null=True, verbose_name='Soup'),
        ),
        migrations.AlterField(
            model_name='restaurantweeklymenu',
            name='third_main',
            field=models.CharField(blank=True, help_text='optional', max_length=200, null=True, verbose_name='Third Main'),
        ),
    ]
