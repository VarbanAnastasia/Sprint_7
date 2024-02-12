import requests
import allure

from constants.urls import Urls

url = Urls.ALL_ORDERS_URL
headers = {"Content-Type": "application/json"}


@allure.feature('Get all orders')
class TestApiAllOrders:

    @allure.story('GET запрос на получение списка всех заказов')
    def test_api_all_orders(self):
        response = requests.request("GET", url, headers=headers)
        assert response.status_code == 200
        result = response.json()
        assert type(result['orders'][0]) == dict
