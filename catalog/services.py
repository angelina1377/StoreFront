from django.core.cache import cache

from .models import Product


def get_products_by_category_cached(category_id, ttl=300):
    """Список всех продуктов в категории с низкоуровневым кешированием.
    Ключ: category_{id}, TTL по умолчанию 300 секунд."""
    cache_key = f"category_{category_id}"
    products = cache.get(cache_key)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id))
        cache.set(cache_key, products, ttl)
    return products


def get_product_cached(product_id, ttl=300):
    """Один продукт по ID с кешированием."""
    cache_key = f"product_{product_id}"
    product = cache.get(cache_key)
    if product is None:
        product = Product.objects.select_related("category").get(pk=product_id)
        cache.set(cache_key, product, ttl)
    return product

