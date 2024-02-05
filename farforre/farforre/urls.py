"""
URL configuration for farforre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import add_to_cart_ajax

urlpatterns = [
    path('', views.index, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('rules/', views.rules, name='rules'),
    path('favorites/', views.favorites, name='favorites'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('get-variant/', views.get_variant, name='get_variant'),
    path('admin/', admin.site.urls),
    path('add-to-cart/', add_to_cart_ajax, name='add-to-cart-ajax'),
    path('cart/', views.cart, name='cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)