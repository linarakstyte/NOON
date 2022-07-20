from django.contrib import admin
from .models import Location, Restaurant, RestaurantWeeklyMenu



class RestaurantWeeklyMenuInline(admin.TabularInline):
    model = RestaurantWeeklyMenu
    can_delete = False

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant_location', 'address')
    search_fields = ('name', 'restaurant_location__location')
    inlines = [RestaurantWeeklyMenuInline]

class RestaurantInline(admin.TabularInline):
    model = Restaurant

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'display_restaurants')
    inlines = [RestaurantInline]


class RestaurantWeeklyMenuAdmin(admin.ModelAdmin):
    model = RestaurantWeeklyMenu
    list_display = ('restaurant', 'weekday', 'visitor')
    list_filter = ('weekday', 'visitor')
    list_editable = ('visitor',)



admin.site.register(Location, LocationAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantWeeklyMenu, RestaurantWeeklyMenuAdmin)


