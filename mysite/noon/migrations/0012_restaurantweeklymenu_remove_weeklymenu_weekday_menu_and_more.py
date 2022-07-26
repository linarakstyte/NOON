# Generated by Django 4.0.6 on 2022-07-09 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noon', '0011_remove_restaurantmenu_dish_restaurantmenu_dessert_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantWeeklyMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soup', models.CharField(help_text='name of the dish', max_length=200, null=True, verbose_name='Soup')),
                ('first_main', models.CharField(help_text='name of the dish', max_length=200, null=True, verbose_name='First Main')),
                ('second_main', models.CharField(help_text='name of the dish', max_length=200, null=True, verbose_name='Second Main')),
                ('third_main', models.CharField(help_text='name of the dish', max_length=200, null=True, verbose_name='Third Main')),
                ('dessert', models.CharField(help_text='name of the dish', max_length=200, null=True, verbose_name='Dessert')),
                ('weekday', models.CharField(blank=True, choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday')], default='1', help_text='Weekday', max_length=1)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noon.restaurant', verbose_name='Restaurant')),
            ],
        ),
        migrations.RemoveField(
            model_name='weeklymenu',
            name='weekday_menu',
        ),
        migrations.DeleteModel(
            name='RestaurantMenu',
        ),
        migrations.DeleteModel(
            name='WeeklyMenu',
        ),
    ]
