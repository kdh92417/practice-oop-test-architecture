import pytest
from oop_code import GrabStore, Product


"""
Unit Test
"""


def test_show_product(adam_store):
    # given
    product_id = 1

    # when
    straw_berry = adam_store.show_product(product_id=product_id)

    # then
    assert straw_berry == Product(name='키보드', price=30000)


def test_take_money(adam_store):
    price = 1000
    pre_money = adam_store._money

    adam_store._take_money(money=price)

    assert adam_store._money == price + pre_money


def test_return_money(adam_store):
    price = 100
    pre_money = adam_store._money

    adam_store._return_money(money=price)

    assert adam_store._money == pre_money - price


def test_take_out_product(adam_store):
    product_id = 1
    product = adam_store._take_out_product(product_id=product_id)

    assert product == Product(name='키보드', price=30000)
    assert not adam_store._products.get(product_id, None)


"""
Integration Test
"""


def test_sell_product_well(adam_store):
    product_id = 1
    pre_money = adam_store._money
    product = adam_store.show_product(product_id=product_id)

    _product = adam_store.sell_product(
        product_id=product_id, money=product.price
    )
    assert adam_store._money == product.price
    assert not adam_store.show_product(product_id=product_id)


def test_sell_product_not_found(adam_store):
    product_id = 100

    with pytest.raises(Exception):
        adam_store.sell_product(product_id=product_id, money=0)
