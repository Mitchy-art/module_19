from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *

# users = ["Ivan", "Andrew", "Petr"]
info = {}


# Create your views here.
def main_page_f(request):
    return render(request, 'fourth_task/main_page.html')


def shop_page_f(request):
    games = Games.objects.all()
    context = {'games': games}
    # context = {
    #     'products': ['Бумага', "Краски", "Карандаши", "Маркеры", "Стёрки", "Мольберты", "Аксессуары", ]
    # }
    return render(request, 'fourth_task/shop_page.html', context)


def cart_page_f(request):
    return render(request, 'fourth_task/cart_page.html')


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            buyers = Buyer.objects.values_list('name')
            if username in buyers:
                info["error"] = 'Пользователь уже существует'
                return render(request, 'fifth_task/registration_page.html', {'info': info})
            elif password != repeat_password:
                info["error"] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', {'info': info})
            elif int(age) < 18:
                info["error"] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', {'info': info})
            else:
                Buyer.objects.create(name=username, age=age, balance=250)
                info['message'] = f'Приветствуем, {username}!'
        info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        buyers = Buyer.objects.values_list('name')
        if username in buyers:
            info["error"] = 'Пользователь уже существует'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        elif password != repeat_password:
            info["error"] = 'Пароли не совпадают'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        elif int(age) < 18:
            info["error"] = 'Вы должны быть старше 18'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        else:
            Buyer.objects.create(name=username, age=age, balance=250)
            info['message'] = f'Приветствуем, {username}!'
    return render(request, 'fifth_task/registration_page.html', info)
