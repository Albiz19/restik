from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Category, Product, Favorite, News
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from .forms import UserProfileForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect



@login_required(login_url='login')  # Указываем здесь имя URL-адреса для страницы входа
def profile_view(request):
    # Проверка на аутентификацию пользователя теперь не нужна, так как login_required сделает это за вас

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_url')  # Используем имя URL-адреса для перенаправления на страницу профиля
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})


def news_view(request):
    news_items = News.objects.all()
    return render(request, 'news.html', {'news_items': news_items})


# Домашняя страница
def home_view(request):
    # Здесь может быть логика для получения данных для домашней страницы, если это необходимо.
    return render(request, 'home.html')


def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu.html', {'categories': categories})

@login_required(login_url='login')
def favorites_view(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})

@login_required(login_url='login')
def remove_from_favorites(request, product_id):
    Favorite.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    is_favorite = False  # Предполагаем, что товар не в избранном

    if request.user.is_authenticated:
        # Проверяем, есть ли продукт в избранном у пользователя
        is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()

    return render(request, 'product_detail.html', {'product': product, 'is_favorite': is_favorite})


@login_required(login_url='login')  # Указываем здесь имя URL-адреса для страницы входа
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)  # Используйте get_or_create для избежания дубликатов
    return redirect('product_detail', product_id=product_id)


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # перенаправление на домашнюю страницу после успешной авторизации
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


# # Обработчик выхода
# from django.contrib.auth import logout
# from django.shortcuts import redirect
#
#
# def logout_view(request):
#     logout(request)
#     # Перенаправление на домашнюю страницу после выхода
#     return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Предполагая, что у вас есть URL с именем 'login'
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# views.py

def logout_view(request):
    logout(request)
    return redirect('home')

