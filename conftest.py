import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

@pytest.fixture()
def courier_methods():
    return CourierMethods()

@pytest.fixture()
def order_methods():
    return OrderMethods()

@pytest.fixture()
def courier(courier_methods):
    login_pass = courier_methods.register_new_courier_and_return_login_password()
    yield login_pass
    response = courier_methods.login_courier(login_pass[0], login_pass[1])
    courier_methods.delete_courier(response.json()['id'])
