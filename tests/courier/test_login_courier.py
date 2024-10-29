import allure
from data import BASE_URL
import requests

class TestLoginCourier:
    @allure.title('Авторизация курьера')
    def test_courier_login(self, courier):
        login_pass, _ = courier
        response = requests.post(f'{BASE_URL}courier/login', json={"login": login_pass[0], "password": login_pass[1]})
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Ошибка при неверных логине и пароле')
    def test_courier_login_invalid_credentials(self):
        payload = {
            "login": "invalid_login",
            "password": "invalid_password"
        }
        response = requests.post(f'{BASE_URL}courier/login', json=payload)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Обязательные поля при авторизации')
    def test_courier_login_missing_fields(self):
        payload = {
            "login": "test_login"
        }
        response = requests.post(f'{BASE_URL}courier/login', json=payload)
        assert response.status_code == 504
