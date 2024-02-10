import requests
import allure

from constants.urls import Urls

url = Urls.ALL_ORDERS_URL
headers = {"Content-Type": "application/json"}


class TestApiAllOrders:

    @allure.feature('Get all orders')
    @allure.story('GET запрос на получение списка всех заказов')
    def test_api_all_orders(self):

        response = requests.request("GET", url, headers=headers)

        assert response.status_code == 200
        print(response.text)
        result = response.json()
        assert type(result['orders'][0]) == dict


