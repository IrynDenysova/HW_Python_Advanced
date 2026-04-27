# Задача 1: Создайте экземпляр движка для подключения к SQLite базе данных в памяти.
# Задача 2: Создайте сессию для взаимодействия с базой данных, используя созданный движок.
# Задача 3: Определите модель продукта Product со следующими типами колонок:
#
# id: числовой идентификатор
# name: строка (макс. 100 символов)
# price: числовое значение с фиксированной точностью
# in_stock: логическое значение
# Задача 4: Определите связанную модель категории Category со следующими типами колонок:
#
# id: числовой идентификатор
# name: строка (макс. 100 символов)
# description: строка (макс. 255 символов)
# Задача 5: Установите связь между таблицами Product и Category с помощью колонки category_id.


import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, NUMERIC
from sqlalchemy.orm import declarative_base, relationship

engine = sqlalchemy.create_engine("sqlite:///test.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(NUMERIC(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))

    product = relationship("Product", backref="category")


Base.metadata.create_all(engine)

# проверка (для себя)

# electronics = Category(name="Электроника", description="Гаджеты и устройства")
# kitchen = Category(name="Кухня", description="Товары для дома")
#
# phone = Product(name="Смартфон", price=59990.00, in_stock=True, category=electronics)
# laptop = Product(name="Ноутбук", price=85000.50, in_stock=False, category=electronics)
# kettle = Product(name="Чайник", price=2500.00, in_stock=True, category=kitchen)
#
# # 2. Добавляем в сессию и сохраняем (commit)
# session.add_all([electronics, kitchen, phone, laptop, kettle])
# session.commit()
