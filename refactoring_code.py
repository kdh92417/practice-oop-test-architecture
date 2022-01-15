from abc import ABC, abstractmethod


class Store(ABC):
    @abstractmethod
    def __init__(self):
        self.name = ""
        self._money = 0
        self._products = {}

    # 1. 상품 보여주기
    @abstractmethod
    def show_product(self, product_id):
        pass

    # 2. 상품을 주기
    @abstractmethod
    def give_product(self, product_id):
        pass

    # 3. 상품대금 받기
    @abstractmethod
    def take_money(self, money):
        pass


class GrabStore(Store):
    def __init__(self, products):
        self._money = 0
        self.name = "그랩마켓"
        self._products = products

    # 해당 매장의 상품 설정
    def set_products(self, products):
        self._products = products

    # 해당 매장의 돈 설정
    def set_money(self, money):
        self._money = money

    # 싱픔 보여주기
    def show_product(self, product_id):
        return self._products[product_id]

    # 상품 주기
    def give_product(self, product_id):
        self._products.pop(product_id)  # products에 product_id를 key로 가지는 value를 삭제한다.

    # 상품 대금 결제
    def take_money(self, money):
        self._money += money


class User:
    # User 객체를 생성할 때 돈과 스토어 객체 변수를 생성
    def __init__(self, money, store: Store):
        self.money = money
        self.store = store
        self.belongs = []

    def get_belongs(self):
        return self.belongs

    def show_product(self, product_id):
        products = self.store.show_product(product_id=product_id)
        return products

    def purchase_product(self, product_id):
        product = self.show_product(product_id=product_id)
        # 스토어 클래스 변수에 직접 접근하지 않고 스토어의 퍼블릭 메서드를 이용하여 클래스변수에 접근
        if self.money >= product["price"]:
            self.store.give_product(product_id=product_id) # 사용자가 꺼내지 않고 스토어에서 꺼내도록 변경
            self.money -= product["price"]  # 사용자가 돈 내기
            self.store.take_money(product['price'])  # 상점에서 돈 받기
            self.belongs.append(product)
            return product
        else:
            raise Exception("잔돈이 부족합니다")


if __name__ == "__main__":
    store = GrabStore(
        products={
            1: {"name": "키보드", "price": 30000},
            2: {"name": "모니터", "price": 50000},
        }
    )
    user = User(money=100000, store=store)
    user.purchase_product(product_id=1)
    print(user.get_belongs())