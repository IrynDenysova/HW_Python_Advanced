# 1. Добавьте в базу данных следующие категории и продукты.
# Добавление категорий: Добавьте в таблицу categories следующие категории:
# Название: "Электроника", Описание: "Гаджеты и устройства."
# Название: "Книги", Описание: "Печатные книги и электронные книги."
# Название: "Одежда", Описание: "Одежда для мужчин и женщин."
# Добавление продуктов: Добавьте в таблицу products следующие продукты, убедившись, что каждый продукт связан с соответствующей категорией:
# Название: "Смартфон", Цена: 299.99, Наличие на складе: True, Категория: Электроника
# Название: "Ноутбук", Цена: 499.99, Наличие на складе: True, Категория: Электроника
# Название: "Научно-фантастический роман", Цена: 15.99, Наличие на складе: True, Категория: Книги
# Название: "Джинсы", Цена: 40.50, Наличие на складе: True, Категория: Одежда
# Название: "Футболка", Цена: 20.00, Наличие на складе: True, Категория: Одежда

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = sqlalchemy.create_engine("sqlite:///test_table.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(DECIMAL(10,2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))

    products = relationship("Product",backref= "category")

if __name__ == '__main__':

    Base.metadata.create_all(engine)

    electronics = Category(name="Электроника", description="Гаджеты и устройства.")
    books = Category(name="Книги", description="Печатные книги и электронные книги.")
    clothing = Category(name="Одежда", description="Одежда для мужчин и женщин.")

    products = [
            Product(name="Смартфон", price=299.99, in_stock=True, category=electronics),
            Product(name="Ноутбук", price=499.99, in_stock=True, category=electronics),
            Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category=books),
            Product(name="Джинсы", price=40.50, in_stock=True, category=clothing),
            Product(name="Футболка", price=20.00, in_stock=True, category=clothing),
        ]


    session.add_all([electronics, books, clothing])
    session.add_all(products)
    session.commit()





