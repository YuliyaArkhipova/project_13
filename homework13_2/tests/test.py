import pytest

from src.classes import Category
from src.classes import Product


@pytest.fixture
def category_fruits():
    return Category('фрукты', 'витамины круглый год', ('апельсины', 'киви', 'виноград'))


def test_init_cat(category_fruits):
    assert category_fruits.name == 'фрукты'
    assert category_fruits.description == 'витамины круглый год'
    assert category_fruits.products == ('апельсины', 'киви', 'виноград')


def test_products(product_fruits):
    assert product_fruits


@pytest.fixture
def product_fruits():
    return Product('апельсины', 'красные', 112.5, 15)


def test_init_prod(product_fruits):
    assert product_fruits.name == 'апельсины'
    assert product_fruits.description == 'красные'
    assert product_fruits.price == 112.5
    assert product_fruits.in_stock == 15


def test_total_category(category_fruits):
    return Category.total_category == 1


def test_total_unique_products(category_fruits):
    return Category.total_unique_products == 6
