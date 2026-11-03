from django.shortcuts import render, get_object_or_404, Http404
from .services import get_products_by_category_cached, get_product_cached
from catalog.models import Category
from .models import Product


def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    # Получаем товары из кеша (они уже отфильтрованы по is_published=True)
    products = get_products_by_category_cached(category_id, ttl=300)

    return render(request, 'catalog/category_products.html', {
        'products': products,
        'category': category,
    })


def product_detail(request, pk):
    product = get_product_cached(pk, ttl=300)

    if not product:
        raise Http404("Товар не найден")

    # ЛОГИКА ДОСТУПА:
    # Товар видим, если:
    # 1. Он опубликован (is_published=True)
    # ИЛИ
    # 2. Пользователь - владелец товара
    # ИЛИ
    # 3. Пользователь - суперпользователь (админ)
    if not product.is_published and not (request.user == product.owner or request.user.is_staff):
        raise Http404("Товар не найден или скрыт")

    return render(request, 'catalog/product_detail.html', {'product': product})


def product_list(request):
    # Показываем только опубликованные товары
    products = Product.objects.filter(is_published=True)
    return render(request, 'catalog/product_list.html', {'products': products})
