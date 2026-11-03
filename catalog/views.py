from django.shortcuts import render, get_object_or_404
from .services import get_products_by_category_cached, get_product_cached
from catalog.models import Category

def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = get_products_by_category_cached(category_id, ttl=300)
    return render(request, 'catalog/category_products.html', {
        'products': products,
        'category': category,
    })

def product_detail(request, pk):
    product = get_product_cached(pk, ttl=300)
    return render(request, 'catalog/product_detail.html', {'product': product})