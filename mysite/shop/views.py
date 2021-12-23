from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *
from .utils import *


menu = [
    {'title': 'Главная', 'url_name': 'main'},
    {'title': 'О нас', 'url_name': 'about'},

]


def index(request):
    cats = Category.objects.all()

    search_query = request.GET.get('search', '')

    if search_query:
        products =Goods.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    else:
        products = Goods.objects.all()

    context = {
        'title': 'Главная',
        'menu': menu,
        'cats': cats,
        'products': products,
    }

    return render(request, 'shop/base.html', context=context)


def about(request):
    context = {
        'title': 'О нас',
        'menu': menu,
    }

    return render(request, 'shop/about.html', context=context)


def main(request):
    return render(request, 'shop/about.html')


def category(request, cat_slug):
    cats = Category.objects.filter(slug=cat_slug)
    products = Goods.objects.filter(cat__slug=cat_slug)

    context = {
        'title': f'Категория {cat_slug}',
        'menu': menu,
        'cats': cats,
        'products': products,
    }

    return render(request, 'shop/categories.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('register')

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('login')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'shop/login.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def thing_def(request, slug_name):
    thing = Goods.objects.get(slug=slug_name)

    context = {
        'title': f'Продукт {thing.title}',
        'menu': menu,
        'thing': thing,
    }

    return render(request, 'shop/product_page.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')
