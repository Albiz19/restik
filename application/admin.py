from django.contrib import admin
from .models import Category, Product, CustomUser, News, RestaurantInfo, Cart, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'on_sale')
    list_filter = ('category', 'on_sale')
    search_fields = ('name',)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone')
    search_fields = ('username', 'email', 'phone')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date')
    search_fields = ('title',)
    date_hierarchy = 'pub_date'


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
    list_display = ('id', 'user', 'product')
    list_filter = ('user', 'product')
    search_fields = ('user__username', 'product__name')
