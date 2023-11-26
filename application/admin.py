from django.contrib import admin
from .models import Category, Product, RestaurantInfo, Cart, Favorite, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'id')
    search_fields = ('title', 'content')
    list_filter = ('published_date',)
    date_hierarchy = 'published_date'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'on_sale')
    list_filter = ('category', 'on_sale')
    search_fields = ('name',)


# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'email', 'phone', 'first_name', 'last_name', 'birth_date')
#     search_fields = ('username', 'email', 'phone', 'first_name', 'last_name')


@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone')
    search_fields = ('name', 'address', 'phone')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    list_filter = ('user', 'product')
    search_fields = ('user__username', 'product__name')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'timestamp')
    list_filter = ('user', 'product')  # или другое поле модели Product, которое вы хотите использовать для фильтрации
    search_fields = ('user__username', 'product__name')
