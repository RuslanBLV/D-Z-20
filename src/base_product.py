# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __repr__(self):
        pass
