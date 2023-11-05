"""java URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from application import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home_view, name='home'),
    path('news/', views.news_view, name='news'),
    path('profile/', views.profile_view, name='profile_url'),
    path("admin/", admin.site.urls),
    path('menu/', views.menu, name='menu'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('login/', views.login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




