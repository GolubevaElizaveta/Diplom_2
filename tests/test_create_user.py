import allure
import pytest
from methods.user import UserMethods
from helpers import create_random_user_data, create_user_data_without_password

user = UserMethods()

class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        """Тестирование успешного создания уникального пользователя."""
        payload = create_random_user_data()
        response = user.create_user(payload)

        assert response.status_code == 200 and response.json().get('success') is True, (
            f'Фактический результат: {response.status_code}, {response.json()}'
        )

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, create_and_delete_user):
        """Тестирование создания пользователя с уже зарегистрированными данными."""
        payload = create_and_delete_user['payload']
        duplicate_response = user.create_user(payload)

        assert duplicate_response.status_code == 403 and duplicate_response.json() == {
            "success": False,
            "message": "User already exists"
        }, f'Фактический результат: {duplicate_response.status_code}, {duplicate_response.json()}'

    @allure.title("Создание пользователя без указания обязательного поля")
    @allure.description("Проверка, что API возвращает ошибку при отсутствии обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_with_missing_field(self, missing_field):
        """Тестирование создания пользователя без указания каждого обязательного поля."""
        payload = create_user_data_without_password()

        # Убираем значение у отсутствующего поля
        if missing_field == "email":
            payload["email"] = ""
        elif missing_field == "password":
            payload["password"] = ""
        elif missing_field == "name":
            payload["name"] = ""

        response = user.create_user(payload)

        expected_response = {
            "success": False,
            "message": "Email, password and name are required fields"
        }

        assert response.status_code == 403 and response.json() == expected_response, (
            f"Ошибка: {missing_field.capitalize()} не был обработан должным образом. "
            f'Фактический результат: {response.status_code}, {response.json()}'
        )