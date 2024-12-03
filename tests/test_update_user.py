import allure
from methods.user import UserMethods
from helpers import create_random_user_data, create_user_data_without_password

user = UserMethods()


class TestUserDataUpdate:
    @allure.title("Успешное изменение данных пользователя с авторизацией")
    @allure.description("Проверка успешного изменения данных пользователя с авторизацией")
    def test_successful_update_with_authorization(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        updated_payload = create_random_user_data()
        updated_payload["password"] = "newpassword!"
        update_response = user.update_user(updated_payload, access_token)
        assert update_response.status_code == 200 and update_response.json().get("success") is True, (
            f'Фактический результат: {update_response.status_code}, {update_response.json()}'
        )

    @allure.title("Неуспешное изменение данных пользователя без авторизации")
    @allure.description("Проверка неуспешного изменения данных пользователя без авторизации")
    def test_failed_update_without_authorization(self):
        updated_payload = create_user_data_without_password()
        updated_payload["password"] = "newpassword!"
        update_response = user.update_user(updated_payload, '')
        expected_message = 'You should be authorised'
        assert update_response.status_code == 401 and update_response.json().get('message') == expected_message, (
            f'Фактический результат: {update_response.status_code}, {update_response.json()}'
        )
