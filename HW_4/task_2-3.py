# Задача 2: Чтение данных.
# Извлеките все записи из таблицы categories.
# Для каждой категории извлеките и выведите все связанные с ней продукты,
# включая их названия и цены.
from task_1 import *

categories = session.query(Category).all()
for category in categories:
    print(category.name)
    for product in category.products:
        print(f"- {product.name}: ${product.price:.2f}")

# Задача 3: Обновление данных.
# Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 349.99.

product = session.query(Product).filter(Product.name == "Смартфон").first()
if product:
    product.price = 349.99
    session.commit()
    print(f"New price: ${product.price}")
