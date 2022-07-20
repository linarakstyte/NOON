# Generated by Django 4.0.6 on 2022-07-07 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text='Input names of the areas in the city', max_length=200, verbose_name='Name of the Area')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(help_text='Describe the restaurant, lunch serving hours and etc', max_length=1000, verbose_name='About')),
                ('address', models.ManyToManyField(help_text="Choose restaurant's location", to='noon.location')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=200, verbose_name='Dish name and description')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant', to='noon.restaurant', verbose_name='Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(blank=True, choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday')], default='1', help_text='Weekday', max_length=1)),
                ('weekday_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noon.restaurantmenu', verbose_name='Menu')),
            ],
        ),
    ]
