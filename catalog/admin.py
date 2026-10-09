from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # Что видно в таблице
    search_fields = ('name',)                  # Поиск по названию
    list_filter = ('price',)                   # Фильтр по цене (опционально)
