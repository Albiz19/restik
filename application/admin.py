from django.contrib import admin
from .models import Category, Product, RestaurantInfo, Cart, Favorite, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Определяет поля, которые будут отображаться в списке объектов в админке
    search_fields = ('name',)  # Поля, по которым можно осуществлять поиск в админке

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'id')  # Отображаемые поля для новостей
    search_fields = ('title', 'content')  # Поля для поиска по новостям
    list_filter = ('published_date',)  # Фильтры для списка новостей
    date_hierarchy = 'published_date'  # Создает иерархию дат для удобной навигации по датам

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'on_sale')  # Отображаемые поля для продуктов
    list_filter = ('category', 'on_sale')  # Фильтры для списка продуктов
    search_fields = ('name',)  # Поля для поиска продуктов

# Пример кода для администратора пользовательской модели (закомментирован)
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'email', 'phone', 'first_name', 'last_name', 'birth_date')
#     search_fields = ('username', 'email', 'phone', 'first_name', 'last_name')

@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone')  # Отображаемые поля для информации о ресторане
    search_fields = ('name', 'address', 'phone')  # Поля для поиска информации о ресторане

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')  # Отображаемые поля для корзины
    list_filter = ('user', 'product')  # Фильтры для списка корзины
    search_fields = ('user__username', 'product__name')  # Поля для поиска в корзине

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'timestamp')  # Отображаемые поля для избранного
    list_filter = ('user', 'product')  # Фильтры для списка избранных товаров
    search_fields = ('user__username', 'product__name')  # Поля для поиска в избранных
