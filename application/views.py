from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Product, Favorite
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm


def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu.html', {'categories': categories})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def add_to_favorites(request, product_id):
    product = Product.objects.get(id=product_id)
    Favorite.objects.create(user=request.user, product=product)
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
