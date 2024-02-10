import allure
import pytest
import requests

from constants.urls import Urls
from constants.user_data import Data

url = Urls.LOGIN_COURIER_URL
headers = {"Content-Type": "application/json"}


class TestApiLoginCourier:
    @allure.feature('Login courier')
    @allure.story('POST запрос на вход курьера в систему')
    @pytest.mark.parametrize(("data", "status_code"), [(Data.data_200_login, 200)])
    def test_api_login_courier_success(self, data, status_code):
        response = requests.request("POST", url, headers=headers, json=data)
        assert response.status_code == status_code
        assert "id" in response.json()

    @allure.feature('Login courier')
    @allure.story('POST запрос на вход курьера в систему')
    @pytest.mark.parametrize(("data", "status_code", "expected_json"),
                             [(Data.data_400_login, 400, {"code": 400, "message": "Недостаточно данных для входа"}),
                              (Data.data_400_without_login_and_password, 400,
                               {"code": 400, "message": "Недостаточно данных для входа"}),
                              (Data.data_400_login_password, 400,
                               {"code": 400, "message": "Недостаточно данных для входа"}),
                              (Data.data_400_login_both, 400, {"code": 400, "message": "Недостаточно данных для входа"})
                              ])
    def test_api_login_courier_fail(self, data, status_code, expected_json):
        response = requests.request("POST", url, headers=headers, json=data)
        assert response.status_code == status_code
        assert response.json() == expected_json
