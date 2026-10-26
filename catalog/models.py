from django.conf import settings
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    # Задание 1: статус публикации
    is_published = models.BooleanField(default=False)
    # Задание 2: владелец продукта
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products'
    )

    class Meta:
        # Задание 1: кастомное право
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]

    def __str__(self):
        return self.name
