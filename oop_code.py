from dataclasses import dataclass
from abc import ABC, abstractmethod

# Create Product Database Class
from typing import Dict


@dataclass
class Product:
    name: str
    price: int


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


class GrabStore(Store):
    def __init__(self, products):
        self._money = 0
        self.name = "그랩마켓"
        self._products = products

    # Specify product type
    def set_products(self, products: Dict[int, Product]):
        self._products = products

    def set_money(self, money: int):
        self._money = money

    def show_product(self, product_id):
        return self._products[product_id]

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
        return self._products.pop(product_id)

    def _take_money(self, money):
        self._money += money

    def _return_money(self, money):
        self._money -= money


class User:
    def __init__(self, money, store: Store):
        self._money = money
        self.store = store
        self._belongs = []

    def get_money(self):
        return self._money

    def get_belongs(self):
        return self._belongs

    def show_product(self, product_id):
        products = self.store.show_product(product_id=product_id)
        return products

    def purchase_product(self, product_id):
        product = self.store.show_product(product_id=product_id)
        price = product.price

        # change private method : self._money >= price -> _check_money_enough()
        if self._check_money_enough(price=price):
            self._give_money(price)

            try:
                my_product = self.store.sell_product(
                    product_id=product_id, money=price)
                self._add_belongs(product)
                return my_product

            except Exception as e:
                self._take_money(money=price)
                print(f"There was a problem during your purchase {str(e)}")
                raise e

        else:
            raise Exception("I don't have enough change")

    # add method
    def _check_money_enough(self, price):
        return self._money >= price

    def _give_money(self, money):
        if not self._check_money_enough(price=money):
            raise Exception('돈이 부족합니다.')
        self._money -= money

    def _take_money(self, money):
        self._money += money

    def _add_belongs(self, product):
        self._belongs.append(product)


if __name__ == "__main__":
    store = GrabStore(
        products={
            1: Product(name='키보드', price=30000),
            2: Product(name='모니터', price=50000),
        }
    )
    user = User(money=50000, store=store)
    user.purchase_product(product_id=1)
    print(user.get_money())
    print(user.get_belongs())
