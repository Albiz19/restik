from django.contrib import admin
from .models import Restaurant, MenuItem

# Регистрация модели Restaurant
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email')
    list_filter = ('name', 'address')
    search_fields = ('name', 'address')
    prepopulated_fields = {'website': ('name',)}

# Регистрация модели MenuItem
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')
