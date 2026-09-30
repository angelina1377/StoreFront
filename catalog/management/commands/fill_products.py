from django.core.management import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Добавляет тестовые продукты, предварительно удаляя существующие данные"

    def handle(self, *args, **options):
        self.stdout.write("Удаляем существующие данные...")
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write("Данные удалены.")

        categories = [
            {"name": "Электроника", "description": "Гаджеты и техника"},
            {"name": "Одежда", "description": "Летняя коллекция"},
        ]

        products = [
            {"name": "Ноутбук", "description": "Игровой ноутбук", "category": "Электроника", "price": "89990.00"},
            {"name": "Смартфон", "description": "Флагманский смартфон", "category": "Электроника", "price": "59990.00"},
            {"name": "Футболка", "description": "Хлопковая футболка", "category": "Одежда", "price": "1990.00"},
        ]

        for cat in categories:
            Category.objects.create(**cat)

        for item in products:
            category = Category.objects.get(name=item.pop("category"))
            Product.objects.create(**item, category=category)

        self.stdout.write(self.style.SUCCESS("Тестовые данные добавлены"))
