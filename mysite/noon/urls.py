from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_restaurants/', views.all_restaurants, name='all_restaurants'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('administration/<int:pk>', views.RestaurantWeeklyMenuUpdateView.as_view(), name='administration_form'),
    path('administration/', views.RestaurantByUserListView.as_view(), name='administration'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('location/<slug:some_slug>', views.location, name='location'),
]