import configuration
import requests
import data

# Фукнция для создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body,
                         headers=data.headers)

# Функция получения заказа по его номеру
def get_order_by_number(track_number):
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH + str(track_number))