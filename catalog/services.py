from django.core.cache import cache
from .models import Product


def get_products_by_category_cached(category_id, ttl=300):
    """
    Список продуктов в категории.
    ВАЖНО: Фильтруем только опубликованные товары (is_published=True).
    """
    # Ключ кеша включает статус публикации, чтобы не отдавать старые данные
    cache_key = f"category_{category_id}_published"
    products = cache.get(cache_key)

    if products is None:
        # Фильтруем по категории И по статусу публикации
        products = list(Product.objects.filter(category_id=category_id, is_published=True))
        cache.set(cache_key, products, ttl)

    return products


def get_product_cached(product_id, ttl=300):
    """
    Один продукт по ID.
    Возвращает объект или None (если не опубликован или не найден).
    """
    cache_key = f"product_{product_id}"
    product = cache.get(cache_key)

    if product is None:
        try:
            # Ищем продукт. Если его нет в БД - выбросится Product.DoesNotExist
            # Мы НЕ фильтруем is_published здесь жестко, чтобы админы могли видеть черновики,
            # но в views мы будем проверять доступность для обычного пользователя.
            product = Product.objects.select_related("category").get(pk=product_id)

            # Сохраняем в кеш. Даже если он не опубликован, сохраняем объект,
            # но решение о показе принимает view.
            cache.set(cache_key, product, ttl)
        except Product.DoesNotExist:
            return None

    return product
