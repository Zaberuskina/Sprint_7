import requests
import random
import string
from data import BASE_URL
import allure

class CourierMethods:
    @allure.step('Регистрация нового курьера и возврат логина и пароля')
    def register_new_courier_and_return_login_password(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{BASE_URL}courier', json=payload)

        login_pass = [login, password, first_name]

        return login_pass, response

    @allure.step('Авторизация курьера')
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{BASE_URL}courier/login', json=payload)
        return response

    @allure.step('Удаление курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(f'{BASE_URL}courier/{courier_id}')
        return response
