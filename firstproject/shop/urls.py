"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from shop.views import listProducts
from shop.views import addProduct, ProductDetail, DeleteProduct, UpdateProduct
from django.contrib import admin


urlpatterns = [
    path('newproduct/', addProduct),

    path('', listProducts.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('<int:pk>/delete', DeleteProduct.as_view(), name='product_delete'),
    path('<int:pk>/update/', UpdateProduct.as_view(), name='product_update'),
    ]

