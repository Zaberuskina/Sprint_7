import requests
from data import BASE_URL
import allure

class TestGetOrders:
    @allure.description('В теле ответа возвращается список заказов')
    def test_get_orders(self):
        response = requests.get(f'{BASE_URL}orders')

        assert response.status_code == 200 and 'orders' in response.json() and isinstance(response.json()['orders'], list) and len(response.json()['orders']) > 0
