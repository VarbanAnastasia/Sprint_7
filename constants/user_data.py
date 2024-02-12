from faker import Faker


fake = Faker(locale="ru_RU")

class Data:
    data_201 = {
        "login": fake.name(),
        "password": "1234",
        "firstName": "ban"
    }

    data_409 = {
        "login": "Anastasia",
        "password": "1234",
        "firstName": "Varban"
    }

    data_400_without_all = {
        "login": "",
        "password": "",
        "firstName": ""
    }

    data_400_without_password_and_first_name = {
        "login": "Varban",
        "password": "",
        "firstName": ""
    }

    data_400_without_login_and_first_name = {
        "login": "",
        "password": "299",
        "firstName": ""
    }

    data_400_without_login_and_password = {
        "login": "",
        "password": "",
        "firstName": "Anastasia"
    }

    data_409_the_same_login = {
        "login": "Varban",
        "password": fake.password(),
        "firstName": fake.name()
    }

    data_200_login = {
            "login": "pumpum",
            "password": "1111"
        }

    data_400_login_password ={
            "login": "",
            "password": "1234"
        }

    data_400_login = {
            "login": "Anastasia",
            "password": ""
        }

    data_400_login_both = {
            "login": "",
            "password": ""
        }

    data_for_order = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    data_add_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

    data_without_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-02-01",
        "comment": "Saske, come back to Konoha"
    }

