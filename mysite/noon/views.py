from datetime import datetime

from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from django.views import generic
from .forms import RestaurantWeeklyMenuForm

from .models import Location, Restaurant, RestaurantWeeklyMenu
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .forms import RestaurantWeeklyMenuForm
from django.views.generic.edit import FormMixin, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


def index(request):
    today = datetime.today().isoweekday()
    restaurants = RestaurantWeeklyMenu.objects.filter(weekday__exact=today)
    day_menus_num = RestaurantWeeklyMenu.objects.filter(weekday__exact=today).count()
    num_iter = list(range(1, day_menus_num + 1))
    grouped_list = zip(num_iter, restaurants)
    context = {
        'grouped_list': grouped_list,       'num_iter': num_iter,
    }
    return render(request, 'index.html', context=context)

def all_restaurants(request):
    num_restaurants = Restaurant.objects.all().count()
    num_iter = list(range(1, num_restaurants+1))
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 8)
    page_number = request.GET.get('page')
    restaurants = paginator.get_page(page_number)

    paginator2 = Paginator(num_iter, 8)
    page_number2 = request.GET.get('page')
    num_iter = paginator2.get_page(page_number2)

    today = datetime.today().isoweekday()
    day_menus = RestaurantWeeklyMenu.objects.filter(weekday__exact=today)
    paginator3 = Paginator(day_menus, 8)
    page_number3 = request.GET.get('page')
    day_menus = paginator3.get_page(page_number3)
    grouped_list = zip(num_iter, restaurants, day_menus)

    context = {
        'grouped_list': grouped_list,
        'num_iter': num_iter,
    }
    return render(request, 'all_restaurants.html', context=context)

def search(request):
    query = request.GET.get('q')
    today = datetime.today().isoweekday()

    search_results_restaurants = RestaurantWeeklyMenu.objects.filter(Q(restaurant__name__icontains=query) & Q(weekday=today))
    search_results_dish = RestaurantWeeklyMenu.objects.filter((Q(soup__icontains=query) | Q(first_main__icontains=query) | Q(second_main__icontains=query) | Q(third_main__icontains=query) | Q(dessert__icontains=query)) & Q(weekday=today))

    num_restaurants = len(search_results_dish)
    num_iter = list(range(1, (num_restaurants + 1)))
    grouped_list = zip(num_iter, search_results_dish)

    num_restaurants2 = len(search_results_restaurants)
    num_iter2 = list(range(1, (num_restaurants2 + 1)))
    grouped_list2 = zip(num_iter2, search_results_restaurants)

    context = {
        'num_iter': num_iter,
        'grouped_list': grouped_list,
        'num_iter2': num_iter2,
        'grouped_list2': grouped_list2
    }

    return render(request, 'search.html', context=context)


def favourites(request):
    query = request.GET.get()
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if restaurant.favourites.filter(id=request.user.ide).exist():
        restaurant.favourites.remove(request.user)
    else:
        restaurant.favourites.add(request.user)

    return render(request, 'profile.html')


@login_required
def profile(request):
    user = request.user
    today = datetime.today().isoweekday()
    number = user.favourites.all().count()
    num_iter = list(range(1, number + 1))
    favourite_restaurants = user.favourites.all()
    menus = RestaurantWeeklyMenu.objects.filter(id=request.user.id)
    grouped_list = zip(num_iter, favourite_restaurants, menus)
    context = {
        'num_iter': num_iter,
        'grouped_list': grouped_list}

    return render(request, 'profile.html', context=context)

def location(request, some_slug):

    restaurants = Restaurant.objects.filter(restaurant_location__location=some_slug)
    menus = RestaurantWeeklyMenu.objects.filter(restaurant__restaurant_location__location=some_slug)
    num_restaurants = len(restaurants)
    num_iter = list(range(1, (num_restaurants + 1)))
    grouped_list = zip(num_iter, restaurants, menus)
    context = {
        'some_slug': some_slug,
        'num_iter': num_iter,
        'grouped_list': grouped_list
    }
    return render(request, 'location.html', context=context)

class RestaurantByUserListView(LoginRequiredMixin, generic.ListView):
    model = RestaurantWeeklyMenu
    template_name = 'administration.html'
    context_object_name = 'menus'

    def get_queryset(self):
        return RestaurantWeeklyMenu.objects.filter(visitor=self.request.user)


class RestaurantWeeklyMenuUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RestaurantWeeklyMenu
    fields = ['soup', 'first_main', 'second_main', 'third_main', 'dessert']
    success_url = "administration"
    template_name = 'administration_form.html'

    def form_valid(self, form):
        form.instance.visitor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        restaurant = self.get_object()
        return self.request.user == restaurant.visitor


@login_required
def user_login(request):
    if request.user.groups.filter(name='restaurants').exists():
        return redirect('/noon/administration')
    elif request.user.groups.filter(name='visitors').exists():
        return redirect('/noon/profile')
    else:
        return render(request, 'login.html', )


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} is taken!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with this email {email} already exists!')
                    return redirect('register')
                else:
                    group = Group.objects.get(name='visitors')
                    User.objects.create_user(username=username, email=email, password=password).groups.add(group)
                messages.error(request, 'Passwords do not match!')
            return redirect('register')
    return render(request, 'register.html')