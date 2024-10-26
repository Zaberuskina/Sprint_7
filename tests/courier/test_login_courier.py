import allure
from data import BASE_URL
import requests

class TestLoginCourier:
    @allure.description('Авторизация курьера')
    def test_courier_login(self, courier_methods):
        login_pass, _ = courier_methods.register_new_courier_and_return_login_password()
        response = courier_methods.login_courier(login_pass[0], login_pass[1])
        assert response.status_code == 200 and 'id' in response.json()

    @allure.description('Ошибка при неверных логине и пароле')
    def test_courier_login_invalid_credentials(self, courier_methods):
        payload = {
            "login": "invalid_login",
            "password": "invalid_password"
        }
        response = requests.post(f'{BASE_URL}courier/login', json=payload)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.description('Обязательные поля при авторизации')
    def test_courier_login_missing_fields(self, courier_methods):
        payload = {
            "login": "test_login"
        }
        response = requests.post(f'{BASE_URL}courier/login', json=payload)
        assert response.status_code == 504
