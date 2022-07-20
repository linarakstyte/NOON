from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from datetime import date
from django.forms import ModelForm

class Location(models.Model):
    location = models.CharField('Name of the Area', max_length=200, help_text='Input names of the areas in the city')

    def display_restaurants(self):
        return ', '.join(location.name for location in self.locations.all()[:3])

    display_restaurants.short_description = 'Restaurants'

    def __str__(self):
        return self.location

class Restaurant(models.Model):
    name = models.CharField('Name', max_length=200)
    restaurant_location = models.ForeignKey('Location', help_text="Choose restaurant's location", on_delete=models.CASCADE, null=True, related_name='locations')
    address = models.CharField('Street address', max_length=200, null=True)
    lunch_hours = models.CharField('Lunch hours', max_length=200, help_text='Lunch serving hours', default="11am - 3pm")
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)

    def __str__(self):
        return f"{self.name}: {self.restaurant_location}, {self.address}, {self.lunch_hours}"

class RestaurantWeeklyMenu(models.Model):
    restaurant = models.ForeignKey(Restaurant, verbose_name='Restaurant', on_delete=models.SET_NULL, null=True, related_name='restaurant')
    soup = models.CharField('Soup', max_length=200, blank=True, null=True)
    first_main = models.CharField('First Main', max_length=200, blank=True, default = 'main')
    second_main = models.CharField('Second Main', max_length=200, blank=True, null=True)
    third_main = models.CharField('Third Main', max_length=200, blank=True, null=True)
    dessert = models.CharField('Dessert', max_length=200, blank=True, null=True)
    visitor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    WEEK_DAYS = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
    )

    weekday = models.CharField(
        max_length=1,
        choices=WEEK_DAYS,
        blank=True,
        default='1',
        help_text='Weekday',
            )

    def __str__(self):
        return f'{self.restaurant}: {self.weekday}'


