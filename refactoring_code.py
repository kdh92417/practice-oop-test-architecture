from abc import ABC, abstractmethod



# 1. Delete take_money()
# 2. Change method : git_product() -> sell_product
class Store(ABC):
    @abstractmethod
    def __init__(self):
        self.name = ""
        self._money = 0
        self._products = {}

    @abstractmethod
    def show_product(self, product_id):
        pass

    # git_product() -> sell_product
    @abstractmethod
    def sell_product(self, product_id, money):
        pass


class GrabStore(Store):
    def __init__(self, products):
        self._money = 0
        self.name = "그랩마켓"
        self._products = products

    def set_products(self, products):
        self._products = products

    def set_money(self, money):
        self._money = money

    def show_product(self, product_id):
        return self._products[product_id]

    # Write sell_product method : give_product() -> sell_product()
    def sell_product(self, product_id, money):

        # Get product
        product = self.show_product(product_id=product_id)

        # Validation 코드 최소화
        if not product:
            raise Exception("The product dose not exist")

        # Receive money to sell goods
        self._take_money(money=money)

        # Logic of sell goods
        try:
            _product = self._take_out_product(product_id=product_id)
            return _product  # if the logic works normally, the product is returned
        except Exception as e:
            self._return_money(money)
            raise e

    # Take out the product
    def _take_out_product(self, product_id):
        return self._products.pop(product_id)

    # 상품 대금 결제
    def _take_money(self, money):
        self._money += money

    # 환불
    def _return_money(self, money):
        self._money -= money


class User:
    # User 객체를 생성할 때 돈과 스토어 객체 변수를 생성
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

    # change methods : give_product(), take_money() -> sell_product()
    # Accessing properties with methods : self.money -= price (x) -> self._give_methods() (O)
    def purchase_product(self, product_id):
        # Product to buy in the store
        product = self.store.show_product(product_id=product_id)
        price = product['price']

        if self._money >= price:
            self._give_money(price)  # Pay for product

            # Logic of purchase
            try:
                my_product = self.store.sell_product(product_id=product_id, money=price)  # Product bought in the store
                self._add_belongs(product)
                return my_product

            except Exception as e:
                self._take_money(money=price)  # return money
                print(f"There was a problem during your purchase {str(e)}")
                raise e

        else:
            raise Exception("I don't have enough change")

    # Add method : pay for product
    def _give_money(self, money):
        self._money -= money

    # Add method : Take the money
    def _take_money(self, money):
        self._money += money

    # Add method : Add product to belongs
    def _add_belongs(self, product):
        self._belongs.append(product)

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