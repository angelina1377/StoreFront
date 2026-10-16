from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('add/', views.product_create, name='add_product'),
    path('<int:pk>/edit/', views.product_update, name='edit_product'),
    path('<int:pk>/delete/', views.product_delete, name='delete_product'),
]
