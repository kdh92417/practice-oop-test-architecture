import pytest
from unittest import mock

from oop_code import (
    GrabStore,
    Product
)
from tests.conftest import API_URL

"""
Unit Test
"""


def test_show_product(mock_api, adam_store, mock_products):
    # given
    product_id = 1
    mock_product = mock_products[product_id]

    # with mock.patch('requests.get') as mock_api:
    #     res = mock_api.return_value
    #     res.status_code = 200
    #     res.json.return_value = mock_product

    # when
    product = adam_store.show_product(product_id=product_id)

    # then
    assert product == Product(
        name=mock_product['title'], price=mock_product['price'])


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


def test_take_out_product(mock_api, adam_store, mock_products):
    # given
    product_id = 1
    mock_product = mock_products[product_id]

    # when
    product = adam_store._take_out_product(product_id=product_id)

    # then
    assert product == Product(name=mock_product['title'], price=mock_product['price'])
    # assert not adam_store._products.get(product_id, None)


"""
Integration Test
"""


def test_sell_product_well(mock_api, adam_store, mock_products):
    product_id = 1
    pre_money = adam_store._money
    mock_product = mock_products[product_id]

    # mocking
    # requests_mock.get(f"{API_URL}{product_id}", json=mock_product)
    # requests_mock.delete(f"{API_URL}{product_id}", json=mock_product)

    product = adam_store.show_product(product_id=product_id)
    _product = adam_store.sell_product(
        product_id=product_id, money=product.price
    )
    assert adam_store._money == product.price
    # assert not adam_store.show_product(product_id=product_id)


def test_sell_product_not_found(mock_api, adam_store, mock_products):
    product_id = 100
    mock_product = mock_products.get(product_id, None)

    # mocking
    # requests_mock.get(f"{API_URL}{product_id}", json=mock_product)
    # requests_mock.delete(f"{API_URL}{product_id}", json=mock_product)

    with pytest.raises(Exception):
        adam_store.sell_product(product_id=product_id, money=0)
