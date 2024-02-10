import requests
from faker import Faker
import allure
import pytest

from constants.urls import Urls
from constants.user_data import Data

fake = Faker(locale="ru_RU")
url = Urls.CREATE_COURIER_URL
headers = {"Content-Type": "application/json"}


class TestApiCreateCourier:
    @allure.feature('Create courier')
    @allure.story('POST запрос на создание нового курьера в системе')
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (
                pytest.param(Data.data_201, 201, {"ok": True})
        )
    ])
    def test_api_create_courier_successful(self, data, status_code, json):
        response = requests.post(url, headers=headers, json=data)
        assert response.status_code == status_code
        assert response.json() == json

    @allure.feature('Create courier')
    @allure.story('POST запрос на создание курьера в сиcтеме дважды')
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (Data.data_409, 409, {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."})
    ])
    def test_api_create_courier_twice(self, data, status_code, json):
        response = requests.request("POST", url, headers=headers, json=data)

        assert response.status_code == status_code
        assert response.json() == json

    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (Data.data_400_without_all, 400, {"code": 400, "message": "Недостаточно данных для создания учетной записи"}),
        (Data.data_400_without_password_and_first_name, 400,
         {"code": 400, "message": "Недостаточно данных для создания учетной записи"}),
        (Data.data_400_without_login_and_first_name, 400,
         {"code": 400, "message": "Недостаточно данных для создания учетной записи"}),
        (Data.data_400_without_login_and_password, 400,
         {"code": 400, "message": "Недостаточно данных для создания учетной записи"})
    ])
    @allure.feature('Create courier')
    @allure.story('POST запрос на создание курьера без обязательного поля пароль')
    def test_api_create_courier_obligatory_fields(self, data, status_code, json):
        response = requests.request("POST", url, headers=headers, json=data)
        assert response.status_code == status_code
        assert response.json() == json

    @allure.feature('Create courier')
    @allure.story('POST запрос на создание курьера c одинаковым логиным')
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (Data.data_409, 409, {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."})
    ])
    def test_api_the_same_login_courier(self, data, status_code, json):
        response = requests.request("POST", url, headers=headers, json=data)
        assert response.status_code == status_code
        assert response.json() == json

