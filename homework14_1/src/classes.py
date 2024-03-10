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
        Category.total_unique_products += len(set(self.__products))

    def __len__(self):
        result = 0
        for i in self.__products:
            result += i.in_stok
        return result

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

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

    def __str__(self):
        return f'{self.name}, {self.price} руб.Остаток: {self.in_stock} шт.'

    def __add__(self, other):
        return self.price * self.in_stock + other.price * other.in_stock

    @classmethod
    def new_product(cls, name, description, price, in_stock, list_products):
        product = cls(name, description, price, in_stock)
        for i in list_products:
            if product.name == i.name:
                i.in_stok += product.in_stock
                if product.price > i.price:
                    i.price = product.price
        else:
            return product

    @property
    def price_new(self):
        return self.price

    @price_new.setter
    def price_new(self, new_price):
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


class ProductsCategory:
    """Класс принимает на вход категорию для прохода по всем товарам категории"""
    def __init_(self, cat):
        self.cat = cat

    def __iter__(self):
        self. current_index = -1
        return self

    def __next__(self):
        if self.current_index + 1 < len(self.cat.products):
            self. current_index += 1
            return self.cat.products(self. current_index).name
        else:
            raise StopIteration

