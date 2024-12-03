import allure
from methods.order import OrderMethods

order = OrderMethods()

class TestGetUserOrders:

    @allure.title("Получение заказов пользователя с авторизацией")
    def test_get_user_orders_with_authorization(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        response = order.get_orders(access_token)
        assert response.status_code == 200 and response.json().get("success") is True, (
            f'Фактический результат: {response.status_code}, {response.json()}'
        )

    @allure.title("Получение заказов пользователя без авторизации")
    def test_get_user_orders_without_authorization(self):
        response = order.get_orders('')
        expected_message = {'success': False, 'message': 'You should be authorised'}
        assert response.status_code == 401 and response.json() == expected_message, (
            f'Фактический результат: {response.status_code}, {response.json()}'
        )
