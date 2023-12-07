from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Category, Product, Favorite, News, Cart
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from .forms import UserProfileForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect



@login_required(login_url='login')
def profile_view(request):

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_url')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})


def news_view(request):
    news_items = News.objects.all()
    return render(request, 'news.html', {'news_items': news_items})


# Домашняя страница
def home_view(request):
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

@login_required(login_url='login')
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

from django.shortcuts import render

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    is_favorite = False
    in_cart = False

    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()
        in_cart = Cart.objects.filter(user=request.user, product=product).exists()

    return render(request, 'product_detail.html', {'product': product, 'is_favorite': is_favorite, 'in_cart': in_cart})

@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product)

    if cart_item.exists():
        cart_item.delete()

    return redirect('product_detail', product_id=product_id)

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if created:
        # Если товар только что добавлен в корзину, установите начальное количество
        cart_item.quantity = 1
        cart_item.save()
    else:
        # Если товар уже в корзине, увеличьте количество
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_detail', product_id=product_id)


@login_required(login_url='login')
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
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
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# views.py

def logout_view(request):
    logout(request)
    return redirect('home')

