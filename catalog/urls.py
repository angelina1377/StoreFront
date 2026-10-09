# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Путь к списку товаров. Имя 'products' обязательно для редиректа.
    path('products/', views.product_list, name='products'),

    # Путь для добавления товара
    path('add/', views.add_product, name='add_product'),
]

