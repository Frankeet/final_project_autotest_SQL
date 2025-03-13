# Илья Карпычев, 27-я когорта — Финальный проект, Автоматизация теста к API. Инженер по тестированию плюс

import sender_stand_request
import data


# Функция для проверки кода ответа
def check_assert_status_code_200(order_body):
        # В переменную order_response сохраняется результат запроса на получение заказа по его номеру:
        order_response = sender_stand_request.get_order_by_number(order_body)     
        # Проверяется, что код ответа равен 200
        assert order_response.status_code == 200

# Тест 1. Результат запроса на получение заказа по его номеру - код ответа равен 200
def test_1_get_order_by_number_positive_response():
      check_assert_status_code_200(data.order_body)