import requests

from typing import Dict
from abc import ABC, abstractmethod

from oop_code import Product


class Store(ABC):
    @abstractmethod
    def __init__(self):
        self.name = ""
        self._money = 0
        self._products = {}

    @abstractmethod
    def show_product(self, product_id):
        pass

    @abstractmethod
    def sell_product(self, product_id, money):
        pass


class AdamRealStore(Store):
    def __init__(self, url="https://fakestoreapi.com"):
        self._money = 0
        self.name = "아담마켓"
        self.url = url

    # Specify product type
    def set_products(self, products: Dict[int, Product]):
        self._products = products

    def set_money(self, money: int):
        self._money = money

    def show_product(self, product_id):
        res = requests.get(url=f"{self.url}/products/{product_id}")
        product = res.json()

        return Product(name=product['title'], price=product['price'])

    def sell_product(self, product_id, money):
        product = self.show_product(product_id=product_id)

        if not product:
            raise Exception("The product dose not exist")

        self._take_money(money=money)

        try:
            _product = self._take_out_product(product_id=product_id)
            return _product
        except Exception as e:
            self._return_money(money)
            raise e

    def _take_out_product(self, product_id):
        res = requests.delete(url=f"{self.url}/products/{product_id}")
        product = res.json()

        return Product(name=product['title'], price=product['price'])

    def _take_money(self, money):
        self._money += money

    def _return_money(self, money):
        self._money -= money


# if __name__ == '__main__':
#     store = AdamStore()
#     result = store.show_product(product_id=10)
#     print(result)
