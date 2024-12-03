import allure
import requests
from data import Urls

class OrderMethods:

    @allure.step("Получение заказов пользователя")
    def get_orders(self, access_token):
        headers = {'Authorization': access_token}
        response = requests.get(Urls.ORDERS_URL, headers=headers)
        return response

    @allure.step("Создание заказа")
    def create_order(self, payload, access_token):
        headers = {'Authorization': access_token}
        response = requests.post(Urls.ORDERS_URL, json=payload, headers=headers)
        return response  # Возвращаем ответ

    @allure.step("Получение доступных ингридиентов")
    def get_ingredients(self):
        response = requests.get(Urls.INGREDIENTS_URL)
        return response.json()