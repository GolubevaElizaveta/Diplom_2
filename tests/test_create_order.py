import allure
import pytest
from methods.order import OrderMethods
from helpers import select_random_ingredients

order = OrderMethods()


class TestCreateOrder:

    @allure.title("Успешное создание заказа с авторизацией и ингредиентами")
    @allure.description("Проверка успешного создания заказа с авторизацией и корректными ингредиентами")
    def test_create_order_with_authorization(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        ingredients = select_random_ingredients()
        response = order.create_order({"ingredients": ingredients}, access_token)
        assert response.status_code == 200 and response.json().get("success") is True, (
            f'Фактический результат: {response.status_code}, {response.json()}'
        )

    @allure.title("Успешное создание заказа без авторизации")
    @allure.description("Проверка успешного создания заказа без авторизации")
    def test_create_order_without_authorization(self):
        ingredients = select_random_ingredients()
        response = order.create_order({"ingredients": ingredients}, "")
        assert response.status_code == 200 and response.json().get("success") is True, (
            f'Фактический результат: {response.status_code}, {response.json()}'
        )

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка неуспешного создания заказа без указания ингредиентов")
    def test_create_order_without_ingredients(self):
        response = order.create_order({"ingredients": []}, "")
        expected_message = "Ingredient ids must be provided"
        assert response.status_code == 400 and response.json()["message"] == expected_message, (
            f'Фактический результат: {response.status_code}, {response.json()}'
        )

    @allure.title("Создание заказа с неверным хэшем ингредиентов")
    @allure.description("Проверка неуспешного создания заказа с неверным хэшем ингредиентов")
    def test_create_order_with_invalid_ingredients(self):
        invalid_ingredient_payload = {
            "ingredients": ["invalid_id_1", "invalid_id_2"]
        }
        response = order.create_order(invalid_ingredient_payload, "")
        expected_message = "One or more ids provided are incorrect"
        assert response.status_code == 400 and response.json()["message"] == expected_message, (
            f'Фактический результат: {response.status_code}, {response.json()}'
        )