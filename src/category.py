from src.product import Product


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
        if not isinstance(product, Product):
            raise TypeError("Добавлять можно только объекты Product или его наследников")
        if not product.in_stock > 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        return self.__products.append(product)

    def average_price_products(self):
        """Метод, который подсчитывает средний ценник всех товаров
        """
        total_price = 0
        for i in self.__products:
            total_price += i.price
        try:
            average_price = total_price/len(self.__products)
            return average_price
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        """Выводит список товаров в формате:
               Продукт, 80 руб. Остаток: 15 шт.
            """
        for i in self.__products:
            print(f"{i.name}, {i.price}. Остаток: {i.in_stok}")
        return None
