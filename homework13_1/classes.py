class Category:
    name: str
    description: str
    products: list

    total_category = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.total_category += 1
        Category.total_unique_products += len(set(self.products))


class Product:
    name: str
    description: str
    price: float
    in_stock: int

    def __init__(self, name, description, price, in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock
