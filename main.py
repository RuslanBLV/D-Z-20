class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
        return products_multiplication_self + products_multiplication_other


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
            self.__products.append(product)
            self.product_count += 1
        else:
            raise ValueError("Можно добавить только продукты")

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
