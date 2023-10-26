from django.shortcuts import render
from .models import Category

def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu.html', {'categories': categories})

