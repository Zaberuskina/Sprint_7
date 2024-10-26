import allure
from data import BASE_URL
import requests

class TestCreateCourier:
    @allure.description('Создание курьера')
    def test_create_courier(self, courier_methods):
        login_pass, response = courier_methods.register_new_courier_and_return_login_password()
        assert len(login_pass) == 3 and response.status_code == 201 and response.json() == {"ok": True}

    @allure.description('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, courier_methods):
        # Создаем курьера и получаем его данные
        login_pass, _ = courier_methods.register_new_courier_and_return_login_password()
        login, password, first_name = login_pass

        # Пытаемся создать курьера с теми же данными
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{BASE_URL}courier', json=payload)

        # Ожидаем, что ответ будет содержать сообщение об ошибке
        assert response.status_code == 409 and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.description('Обязательные поля при создании курьера')
    def test_create_courier_missing_fields(self, courier_methods):
        payload = {
            "login": "test_login",
            "firstName": "test_name"
        }
        response = requests.post(f'{BASE_URL}courier', json=payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'
