import pytest
from oop_code import GrabStore, Product, User


# scope : 한번 만 값 반환 or 반복적으로 값 반환
@pytest.fixture(scope="function")
def adam_store():
    return GrabStore(
        products={
            1: Product(name='키보드', price=30000),
            2: Product(name='모니터', price=50000),
        }
    )


@pytest.fixture(scope="function")
def user(adam_store):
    return User(money=150000, store=adam_store)
