from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registrations.html', context)

def profile(request):
    if request.method == 'POST':
        print("POST data:", request.POST)  # Добавьте для отладки
        print("FILES:", request.FILES)    # Проверка загрузки файлов
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Форма не валидна. Ошибки:", form.errors)  # Добавьте эту строку
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Store - профиль', 'form': form}
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))