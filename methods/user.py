import allure
import requests
from data import Urls

class UserMethods:

    @allure.step("Создание пользователя")
    def create_user(self, payload):
        response = requests.post(Urls.REGISTER_URL, json=payload)
        return response

    @allure.step("Авторизация пользователя")
    def login_user(self, payload):
        response = requests.post(Urls.LOGIN_URL, json=payload)
        return response

    @allure.step("Получение информации о пользователе")
    def get_user_info(self, access_token):
        headers = {'Authorization': access_token}
        response = requests.get(Urls.USER_URL, headers=headers)
        return response

    @allure.step("Изменение данных пользователя")
    def update_user(self, payload, access_token):
        headers = {'Authorization': access_token}
        response = requests.patch(Urls.USER_URL, json=payload, headers=headers)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, access_token):
        headers = {'Authorization': access_token}
        response = requests.delete(Urls.USER_URL, headers=headers)
        return response