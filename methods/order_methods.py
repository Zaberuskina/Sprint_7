import requests
from data import BASE_URL
import allure
class OrderMethods:
    @allure.step('Создание заказа')
    def post_order(self, order_data):
        response = requests.post(f'{BASE_URL}orders', json=order_data)
        return response.status_code, response.json()
