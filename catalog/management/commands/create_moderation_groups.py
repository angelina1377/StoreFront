from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission  # <-- ЭТОГО НЕ ХВАТАЛО
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" и назначает ей права'

    def handle(self, *args, **options):
        # Получаем ContentType именно для модели Product
        product_ct = ContentType.objects.get_for_model(Product)

        # Группа "Модератор продуктов"
        mod_group, _ = Group.objects.get_or_create(name='Модератор продуктов')

        # Встроенное право на удаление продуктов (строго для модели Product)
        delete_perm = Permission.objects.get(
            content_type=product_ct,
            codename='delete_product'
        )

        # Кастомное право на отмену публикации
        unpublish_perm = Permission.objects.get(
            content_type=product_ct,
            codename='can_unpublish_product'
        )

        mod_group.permissions.add(delete_perm, unpublish_perm)

        self.stdout.write(
            self.style.SUCCESS('Группа "Модератор продуктов" успешно создана/обновлена, права назначены.')
        )

        mod_group.permissions.add(delete_perm, unpublish_perm)

        self.stdout.write(
            self.style.SUCCESS('Группа "Модератор продуктов" успешно создана/обновлена, права назначены.')
        )
