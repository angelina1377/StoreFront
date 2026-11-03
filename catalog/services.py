from django.core.cache import cache
from catalog.models import Product


def get_products_by_category_cached(category_id, ttl=300):
    cache_key = f"category_{category_id}"
    data = cache.get(cache_key)
    if data is not None:
        return data

    product = Product.objects.select_related('category').get(pk=product_id)
    cache.set(cache_key, product, ttl)
    return product
