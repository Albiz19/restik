from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu.html', {'categories': categories})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

