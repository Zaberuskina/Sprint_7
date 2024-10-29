BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'

BASE_ORDER_DATA = {
    "firstName": "Максим",
    "lastName": "Пупкин",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Спасибо"
}

ORDER_DATA_1 = BASE_ORDER_DATA.copy()
ORDER_DATA_1["color"] = ["BLACK"]

ORDER_DATA_2 = BASE_ORDER_DATA.copy()
ORDER_DATA_2["color"] = ["BLACK", "GREY"]