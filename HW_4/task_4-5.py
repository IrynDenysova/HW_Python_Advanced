from task_1 import *
from sqlalchemy import func

# Задача 4: Агрегация и группировка
# Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой категории.

total_products  = session.query(Category,func.count(Product.id)).join(Product).group_by(Category.name).all()
for category, count in total_products:
    print(f"{category.name}: {count}")

# Задача 5: Группировка с фильтрацией
# Отфильтруйте и выведите только те категории, в которых более одного продукта.

filtered_categories = session.query(Category,func.count(
    Product.id)).join(Product).group_by(Category.name).having(func.count(Product.id) > 1).all()
for category,count in filtered_categories:
    print(category.name)










