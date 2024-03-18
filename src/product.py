from abc import ABC, abstractmethod


class ProductAbc(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls):
        pass


class MixinLog:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v}'
        return f"Создан объект со свойствами {object_attributes}"


class Product(MixinLog, ProductAbc):
    name: str  # название
    description: str  # описание
    price: float  # цена
    in_stock: int  # количество в наличии

    def __init__(self, name, description, price, in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.price} руб.Остаток: {self.in_stock} шт.'

    def __add__(self, other):
        if type(other) == type(self):
            return self.price * self.in_stock + other.price * other.in_stock
        else:
            raise TypeError

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


class Smartphone(Product):
    efficiency: str  # производительность
    model: str  # модель
    amount_internal_memory: float  # объем встроенной памяти
    color: str  # цвет

    def __init__(self, name, description, price, in_stock, efficiency, model, amount_internal_memory, color):
        super().__init__(name, description, price, in_stock)
        self.efficiency = efficiency
        self.model = model
        self.amount_internal_memory = amount_internal_memory
        self.color = color


class LawnGrass(Product):
    country: str  # страна-производитель
    germination_period: float  # срок прорастания
    color: str  # цвет

    def __init__(self, name, description, price, in_stock, country, germination_period, color):
        super().__init__(name, description, price, in_stock)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class ProductsCategory:
    """Класс принимает на вход категорию для прохода по всем товарам категории"""
    def __init__(self, cat):
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
