from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass
import unittest
import pytest


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    def test_product_attributes(self):
        self.assertEqual(self.product1.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(self.product1.description, "256GB, Серый цвет, 200MP камера")
        self.assertEqual(self.product1.price, 180000.0)
        self.assertEqual(self.product1.quantity, 5)

        self.assertEqual(self.product2.name, "Iphone 15")
        self.assertEqual(self.product2.description, "512GB, Gray space")
        self.assertEqual(self.product2.price, 210000.0)
        self.assertEqual(self.product2.quantity, 8)

        self.assertEqual(self.product3.name, "Xiaomi Redmi Note 11")
        self.assertEqual(self.product3.description, "1024GB, Синий")
        self.assertEqual(self.product3.price, 31000.0)
        self.assertEqual(self.product3.quantity, 14)


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        self.category1 = Category("Смартфоны",
                                  "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                                  "функций для удобства жизни",
                                  [self.product1, self.product2, self.product3])

    def test_category_attributes(self):
        self.assertEqual(self.category1.name, "Смартфоны")
        self.assertEqual(self.category1.description,
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                         "удобства жизни")


@pytest.fixture()
def dict_product():
    dict_product = {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0, "quantity": 5}
    return dict_product


def test_product_new_product(dict_product):
    new_product1 = Product.new_product(dict_product)
    assert new_product1.name == "Samsung Galaxy S23 Ultra"
    assert new_product1.description == "256GB, Серый цвет, 200MP камера"
    assert new_product1.price == 180000.0
    assert new_product1.quantity == 5


def test_add_product():
    new_product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    new_product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    new_product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert new_product1 + new_product2 == 2580000.0
    assert new_product1 + new_product3 == 1334000.0
    assert new_product2 + new_product3 == 2114000.0


def test_smartphone_product():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024,
                             "Синий")
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"

    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"

    assert smartphone3.name == "Xiaomi Redmi Note 11"
    assert smartphone3.description == "1024GB, Синий"
    assert smartphone3.price == 31000.0
    assert smartphone3.quantity == 14
    assert smartphone3.efficiency == 90.3
    assert smartphone3.model == "Note 11"
    assert smartphone3.memory == 1024
    assert smartphone3.color == "Синий"


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                                      "S23 Ultra", 256, "Серый")
        self.smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
        self.smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024,
                                      "Синий")

    def test_smartphone_attributes(self):
        self.assertEqual(self.smartphone1.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(self.smartphone1.description, "256GB, Серый цвет, 200MP камера")
        self.assertEqual(self.smartphone1.price, 180000.0)
        self.assertEqual(self.smartphone1.quantity, 5)
        self.assertEqual(self.smartphone1.efficiency, 95.5)
        self.assertEqual(self.smartphone1.model, "S23 Ultra")
        self.assertEqual(self.smartphone1.memory, 256)
        self.assertEqual(self.smartphone1.color, "Серый")

        self.assertEqual(self.smartphone2.name, "Iphone 15")
        self.assertEqual(self.smartphone2.description, "512GB, Gray space")
        self.assertEqual(self.smartphone2.price, 210000.0)
        self.assertEqual(self.smartphone2.quantity, 8)
        self.assertEqual(self.smartphone2.efficiency, 98.2)
        self.assertEqual(self.smartphone2.model, "15")
        self.assertEqual(self.smartphone2.memory, 512)
        self.assertEqual(self.smartphone2.color, "Gray space")

        self.assertEqual(self.smartphone3.name, "Xiaomi Redmi Note 11")
        self.assertEqual(self.smartphone3.description, "1024GB, Синий")
        self.assertEqual(self.smartphone3.price, 31000.0)
        self.assertEqual(self.smartphone3.quantity, 14)
        self.assertEqual(self.smartphone3.efficiency, 90.3)
        self.assertEqual(self.smartphone3.model, "Note 11")
        self.assertEqual(self.smartphone3.memory, 1024)
        self.assertEqual(self.smartphone3.color, "Синий")


def test_lawnGrass_product():
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"

    assert grass2.name == "Газонная трава 2"
    assert grass2.description == "Выносливая трава"
    assert grass2.price == 450.0
    assert grass2.quantity == 15
    assert grass2.country == "США"
    assert grass2.germination_period == "5 дней"
    assert grass2.color == "Темно-зеленый"


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        self.grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
        self.grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    def test_lawnGrass_attributes(self):
        self.assertEqual(self.grass1.name, "Газонная трава")
        self.assertEqual(self.grass1.description, "Элитная трава для газона")
        self.assertEqual(self.grass1.price, 500.0)
        self.assertEqual(self.grass1.quantity, 20)
        self.assertEqual(self.grass1.country, "Россия")
        self.assertEqual(self.grass1.germination_period, "7 дней")
        self.assertEqual(self.grass1.color, "Зеленый")

        self.assertEqual(self.grass2.name, "Газонная трава 2")
        self.assertEqual(self.grass2.description, "Выносливая трава")
        self.assertEqual(self.grass2.price, 450.0)
        self.assertEqual(self.grass2.quantity, 15)
        self.assertEqual(self.grass2.country, "США")
        self.assertEqual(self.grass2.germination_period, "5 дней")
        self.assertEqual(self.grass2.color, "Темно-зеленый")


def test_product_str():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    assert str(smartphone1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(smartphone2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(smartphone3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_category_str():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                                      "функций для удобства жизни", [product1, product2, product3])
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_mixin_log(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    messange = capsys.readouterr()
    assert messange.out.strip() == "Product('Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5')"


def test_error():
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_middle_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    assert category1.middle_price() == 140333.33
