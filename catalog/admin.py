from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # В список выводим только текстовые поля и цену. Картинку так выводить нельзя.
    list_display = ('name', 'price', 'has_image')
    search_fields = ('name',)
    list_filter = ('price',)

    # Этот метод нужен, чтобы красиво показать наличие картинки в таблице
    def has_image(self, obj):
        if obj.image:
            return "✅ Есть фото"
        return "❌ Нет фото"

    # Даем понятное название колонке вместо имени метода
    has_image.short_description = 'Фото'

