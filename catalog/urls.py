from django.urls import path
from . import views

urlpatterns = [
    # ... другие пути
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

]
