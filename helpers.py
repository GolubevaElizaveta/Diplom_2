from faker import Faker
import random
from methods.order import OrderMethods

fake = Faker()
order = OrderMethods()

def create_random_user_data():
    unique_email = f"{fake.email().split('@')[0]}_{random.randint(1000, 9999)}@example.com"
    return {
        "email": unique_email,
        "password": fake.password(),
        "name": fake.name()
    }


def create_user_data_without_password():
    """Создание данных пользователя без обязательного поля (пароля)."""
    return {
        "email": fake.email(),
        "name": fake.name()
        # Поле "password" отсутствует
    }
 # Неверные учетные данные
def create_invalid_credentials():
    return {
        "email": fake.email(),
        "password": fake.password()
    }

 # Случайные ингридиенты
def select_random_ingredients():
    ingredients_data = order.get_ingredients()
    buns = [item['_id'] for item in ingredients_data['data'] if item['type'] == 'bun']
    mains = [item['_id'] for item in ingredients_data['data'] if item['type'] == 'main']
    return [random.choice(buns), random.choice(mains)]