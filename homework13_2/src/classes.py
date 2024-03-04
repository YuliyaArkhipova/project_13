class Category:
    name: str  # название
    description: str  # описание
    products: list  # товары

    total_category = 0  # общее количество категорий
    total_unique_products = 0  # общее количество уникальных продуктов

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_category += 1
        Category.total_unique_products += len(set(self.products))

    def add_product(self, product):
        """ Метод принимает на вход объект товара и добавляет его в список
     """
        return self.__products.append(product)


@property
def products(self):
    """Выводит список товаров в формате:
    Продукт, 80 руб. Остаток: 15 шт.
    """
    for i in self.__products:
        print(f"{i.name}, {i.price}. Остаток: {i.in_stok}")
    return None


class Product:
    name: str  # название
    description: str  # описание
    price: float  # цена
    in_stock: int  # количество в наличии

    def __init__(self, name, description, price, in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock

    @classmethod
    def new_product(cls, name, description, price, in_stock, list_products):
        product = cls(name, description, price, in_stock)
        for i in list_products:
            if product.name == i.name:
               i.in_stok += product.in_stock
               if product.price > i.price:
                i.price = product.price
        else:
            list_products.append(product)
        return list_products

@property
def price(self):
    return self.price


@price.setter
def prise(self, new_price):
    """Метод подтверждения пользователем понижения цены
    """
    if new_price > 0:
        if self.price > new_price:
            user_response = input('Если Вы согласны понизить цену, введите "y"').lower()
            if user_response == "y":
                self.price = new_price
        else:
            self.price = new_price
    else:
        print('Введена некорректная цена')





