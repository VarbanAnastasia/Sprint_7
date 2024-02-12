import requests
import allure
import pytest

from constants.urls import Urls
from constants.user_data import Data

url = Urls.ALL_ORDERS_URL
headers = {"Content-Type": "application/json"}


@allure.feature('Create order')
class TestApiCreateOrder:

    @allure.feature('Create order')
    @allure.title('POST запрос на создание заказа')
    @pytest.mark.parametrize(("data", "status_code"), [
        (Data.data_for_order, 201),
        (Data.data_without_color, 201),
        (Data.data_add_color, 201),
    ])
    def test_api_create_order(self, data, status_code):

        response = requests.request("POST", url, headers=headers, json=data)

        assert response.status_code == status_code
        assert 'track' in response.json()
