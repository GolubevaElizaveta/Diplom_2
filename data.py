class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    LOGIN_URL = f'{BASE_URL}auth/login'  # авторизация пользователя
    REGISTER_URL = f'{BASE_URL}auth/register'  # создание пользователя/регистрация
    USER_URL = f'{BASE_URL}auth/user'  # данные о пользователе и удаление пользователя
    ORDERS_URL = f'{BASE_URL}orders'  # создание заказа и заказы конкретного пользователя
    INGREDIENTS_URL = f'{BASE_URL}ingredients'  # получение данных об ингредиентах