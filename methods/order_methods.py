import requests
from data import BASE_URL

class OrderMethods:

    def post_order(self, order_data):
        response = requests.post(f'{BASE_URL}orders', json=order_data)
        return response.status_code, response.json()
