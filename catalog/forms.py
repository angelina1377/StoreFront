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
        # Только те поля, что есть в модели
        fields = ['name', 'description', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название продукта'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'rows': 4, 'placeholder': 'Описание продукта'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Цена'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if not name:
            return name
        text = name.lower()
        for word in FORBIDDEN_WORDS:
            if word in text:
                raise ValidationError(f'В названии нельзя использовать слово "{word}".')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if not description:
            return description
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
        if image:
            if '.' not in image.name:
                raise forms.ValidationError('Файл должен иметь расширение.')

            ext = image.name.split('.')[-1].lower()
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']

            if ext not in valid_extensions:
                raise forms.ValidationError('Допустимы только изображения: jpg, jpeg, png, gif.')
        return image
