import requests
import configuration


def post_new_order():
    url = configuration.URL + configuration.CREATE_ORDER_PATH
    body = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Прекрасная Россия будущего",
        "metroStation": "4",
        "phone": "12345678910",
        "rentTime": 5,
        "deliveryDate": "2023-08-29",
        "comment": "Хоспаде, куда я жмал",
        "color": "BLACK"
    }
    
    return requests.post(url, json=body, headers=configuration.HEADERS)


def get_order_by_track(track_number):
    url = configuration.URL + configuration.GET_ORDER_BY_TRACK_PATH + "?t=" + str(track_number)
    return requests.get(url, headers=configuration.HEADERS)
