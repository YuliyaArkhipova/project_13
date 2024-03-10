import pytest

from src.classes import Category
from src.classes import Product
from src.classes import Smartphone
from src.classes import LawnGrass

@pytest.fixture
def category_smart():
    return Category('Смартфоны', 'Смартфоны, как средство не только коммуникации', ('Samsung', 'Iphone', 'Xiaomi'))

@pytest.fixture
def product_smart():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)

def test_init_cat(category_smart):
    assert category_smart.name == 'Смартфоны'
    assert category_smart.description == 'Смартфоны, как средство не только коммуникации'
    assert category_smart.products == ('Samsung', 'Iphone', 'Xiaomi')


def test_products(product_smart):
    assert product_smart

def test_init_prod(product_smart):
    assert product_smart.name == 'Samsung Galaxy C23 Ultra'
    assert product_smart.description == '256GB, Серый цвет, 200MP камера'
    assert product_smart.price == 180000.0
    assert product_smart.in_stock == 5


def test_total_category(category_smart):
    return Category.total_category == 1


def test_total_unique_products(category_smart):
    return Category.total_unique_products == 6
