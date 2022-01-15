from abc import ABC, abstractmethod


class Store(ABC):
    @abstractmethod
    def __init__(self):
        self.name = ""
        self.money = 0
        self.products = {}

    @abstractmethod
    def set_money(self, money):
        pass

    @abstractmethod
    def set_products(self, products):
        pass

    @abstractmethod
    def get_money(self):
        pass

    @abstractmethod
    def get_products(self):
        pass


class GrabStore(Store):
    def __init__(self):
        self.money = 0
        self.name = "그랩마켓"
        self.products = {
            1: {"name": "키보드", "price": 30000},
            2: {"name": "모니터", "price": 50000},
        }

    def set_money(self, money):
        self.money = money

    def set_products(self, products):
        self.products = products

    def get_money(self):
        return self.money

    def get_products(self):
        return self.products


class User:
    # Store 추상클래스를 파라미터로 의존성 주입
    def __init__(self, store: Store):
        self.money = 0
        self.store = GrabStore()
        self.belongs = []

    def set_money(self, money):
        self.money = money

    def set_belongs(self, belongs):
        self.belongs = belongs

    def get_money(self):
        return self.money

    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.store

    def see_product(self, product_id):
        products = self.store.get_products()
        return products[product_id]


if __name__ == "__main__":
    user_a = User(GrabStore)
    print(user_a.store.get_products())