from django.shortcuts import render
from .models import Product, Contact  # Добавлен импорт обеих моделей

def home(request):
    last_products = Product.objects.order_by("-created_at")[:5]
    for product in last_products:
        print(product.name)
    return render(request, "catalog/home.html", {"last_products": last_products})

def contacts(request):
    contact = Contact.objects.first()  # Получаем первый контакт из БД
    success = False
    if request.method == 'POST':
        success = True
    return render(request, 'catalog/contacts.html', {'contact': contact, 'success': success})
