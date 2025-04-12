# -*- coding: utf-8 -*-
from src.base_product import BaseProduct
from src.mixin_log import MixinLog


class Product(MixinLog, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        elif value <= 0:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, dict_products):
        name = dict_products["name"]
        description = dict_products["description"]
        price = dict_products["price"]
        quantity = dict_products["quantity"]
        new_products = Product(name, description, price, quantity)
        return new_products

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        products_multiplication_self = self.__price * self.quantity
        products_multiplication_other = other.__price * other.quantity
        if isinstance(other, self.__class__):
            return products_multiplication_self + products_multiplication_other
        else:
            raise TypeError
