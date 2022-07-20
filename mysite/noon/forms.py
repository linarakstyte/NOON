from django.forms import ModelForm

from .models import RestaurantWeeklyMenu
from django import forms
from django.contrib.auth.models import User

class RestaurantWeeklyMenuForm(forms.ModelForm):
    class Meta:
        model = RestaurantWeeklyMenu
        fields = ['soup', 'first_main', 'second_main', 'third_main', 'dessert']
        widgets = {'restaurant': forms.HiddenInput(), 'visitor': forms.HiddenInput(), 'weekday': forms.HiddenInput()}

