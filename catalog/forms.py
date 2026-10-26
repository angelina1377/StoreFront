from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'is_published']
        labels = {
            'name': 'Название продукта',
            'is_published': 'Опубликован',
        }
