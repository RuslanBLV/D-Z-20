from main import Product, Category
import unittest


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
        self.assertEqual(len(self.category1.products), 3)
