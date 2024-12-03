import pytest
from faker import Faker
from methods.user import UserMethods
from helpers import create_random_user_data

fake = Faker()
user = UserMethods()

@pytest.fixture
def create_and_delete_user():
    payload = create_random_user_data()  # Генерация данных нового пользователя
    created_response = user.create_user(payload)  # Создание пользователя
    if created_response.status_code == 200:
        # Проверяем, что ответ содержит токен доступа
        access_token = created_response.json().get('accessToken')  # Используем get для безопасного доступа
        assert access_token is not None, "Токен доступа не был получен"  # Проверяем, что токен существует

        yield {
            'response': created_response,
            'payload': payload,
            'access_token': access_token  # Возвращаем токен доступа
        }
        user.delete_user(access_token)  # Удаление пользователя после теста
    else:
        yield {
            'response': created_response,
            'payload': payload
        }