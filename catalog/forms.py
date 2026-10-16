import os
from django import forms
from django.core.exceptions import ValidationError
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 4, 'placeholder': 'Описание продукта'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Цена'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        text = name.lower()
        for word in FORBIDDEN_WORDS:
            if word in text:
                raise ValidationError(f'В названии нельзя использовать слово "{word}".')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        text = description.lower()
        for word in FORBIDDEN_WORDS:
            if word in text:
                raise ValidationError(f'В описании нельзя использовать слово "{word}".')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return image
        allowed_exts = ['.jpg', '.jpeg', '.png']
        max_size_mb = 5
        ext = os.path.splitext(image.name).lower()
        if ext not in allowed_exts:
            raise ValidationError('Разрешены только файлы JPEG и PNG.')
        if image.size > max_size_mb * 1024 * 1024:
            raise ValidationError(f'Размер файла не должен превышать {max_size_mb} МБ.')
        return image

