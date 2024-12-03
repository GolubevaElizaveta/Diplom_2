import allure
import requests
import json
from methods.user import UserMethods
from helpers import create_user_data_without_password
from data import Urls

user = UserMethods()


class TestUserLogin:
    @allure.title('Успешная авторизация зарегистрированного пользователя')
    def test_successful_login_existing_user(self, create_and_delete_user):
        response = create_and_delete_user['response']
        if response.status_code != 200:
            print(f"Ошибка при создании пользователя: {response.status_code}, {response.text}")
            assert False, "Пользователь не был создан"
        payload = {
            "email": create_and_delete_user['payload']["email"],
            "password": create_and_delete_user['payload']["password"]
        }
        headers = {"Content-type": "application/json"}
        login_response = requests.post(Urls.LOGIN_URL, headers=headers, data=json.dumps(payload))
        assert login_response.status_code == 200 and login_response.json().get("success") is True, (
            f'Фактический результат: {login_response.status_code}, {login_response.json()}'
        )

    @allure.title('Неуспешная авторизация с неверным логином и паролем')
    def test_failed_login_with_invalid_credentials(self):
        invalid_user_data = create_user_data_without_password()
        payload = {
            "email": invalid_user_data["email"] + '1',  # Неверный email
            "password": "invalidpassword"  # Неверный пароль
        }
        headers = {"Content-type": "application/json"}
        response = requests.post(Urls.LOGIN_URL, headers=headers, data=json.dumps(payload))
        expected_result = {'success': False, 'message': 'email or password are incorrect'}
        assert response.status_code == 401 and response.json() == expected_result, (
            f'Фактический результат: {response.status_code}, {response.json()}'
        )