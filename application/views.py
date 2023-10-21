from django.shortcuts import render
from .models import Restaurant, MenuItem

def menu_view(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'menu.html', {'restaurants': restaurants})

