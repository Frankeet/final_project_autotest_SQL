import configuration
import requests
import data

# Фукнция для создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body,
                         headers=data.headers)

# Функция получения номера заказа
def get_order_number(order_body):
    return post_new_order(order_body).json()['track']

# Функция получения заказа по его номеру
def get_order_by_number(order_body):
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH + str(get_order_number(order_body)))