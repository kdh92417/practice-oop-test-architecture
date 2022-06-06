import pytest
from oop_code import GrabStore, Product, User
from real_adam_store import AdamRealStore

API_URL = "https://fakestoreapi.com/products/"

@pytest.fixture(scope="function")
def mock_products():
    return {
        1: {'title': '키보드', 'price': 30000},  # Cheap
        2: {'title': '모니터', 'price': 5000000},  # Expensive
    }

# scope : 한번 만 값 반환 or 반복적으로 값 반환


@pytest.fixture(scope="function")
def adam_store():
    return AdamRealStore()


@pytest.fixture(scope="function")
def user(adam_store):
    return User(money=150000, store=adam_store)
