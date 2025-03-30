import pytest
from main import Product, Category


@pytest.fixture()
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product(product):
    assert product.name == 'Samsung Galaxy S23 Ultra'
    assert product.description == '256GB, Серый цвет, 200MP камера'
    assert product.price == 180000.0
    assert product.quantity == 5


@pytest.fixture()
def category():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения "
                                 "дополнительных функций для удобства жизни", [product1, product2, product3])


def test_category(category):
    assert (category.name == "Смартфоны") == True
    assert category.description == ("Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                                    "функций для удобства жизни")
    assert len(category.products) == 3
    assert category.category_count == 1
    assert category.product_count == 3


@pytest.fixture()
def category1():
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    return Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим "
                                  "другом и помощником", [product4])


def test_category1(category1):
    assert category1.name == "Телевизоры"
    assert category1.description == ("Современный телевизор, который позволяет наслаждаться просмотром, станет вашим "
                                     "другом и помощником")
    assert len(category1.products) == 1
    assert (category1.products == category1.products) == True
    assert category1.category_count == 1
    assert category1.product_count == 1
