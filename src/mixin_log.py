# -*- coding: utf-8 -*-
from abc import ABC
from src.base_product import BaseProduct


class MixinLog(BaseProduct, ABC):
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.description}, {self.price}, {self.quantity}')"