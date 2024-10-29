from data import ORDER_DATA_1, ORDER_DATA_2, BASE_ORDER_DATA
import allure
from methods.order_methods import OrderMethods

class TestCreateOrder:
    @allure.title('Можно указать один из цветов в заказе')
    def test_create_order(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.post_order(ORDER_DATA_1)
        assert status_code == 201 and 'track' in response_context

    @allure.title('Можно указать оба цвета в заказе')
    def test_create_order_with_both_colors(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.post_order(ORDER_DATA_2)
        assert status_code == 201 and 'track' in response_context

    @allure.title('Можно не указывать цвет в заказе')
    def test_create_order_without_color(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.post_order(BASE_ORDER_DATA)
        assert status_code == 201 and 'track' in response_context
