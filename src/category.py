# -*- coding: utf-8 -*-
from src.product import Product


class Category:
    category_count = 0
    product_count = 0
    name: str
    description: str
    products: list[Product]

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)


    @property
    def products(self):
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products])

    def add_product(self, product):
        if isinstance(product, Product):
            if issubclass(type(product), Product):
                self.__products.append(product)
                self.product_count += 1
            else:
                raise TypeError
        else:
            raise TypeError

    def __str__(self):
        count_sum = 0
        for i in self.__products:
            count_sum += i.quantity
        return f"{self.name}, количество продуктов: {count_sum} шт."