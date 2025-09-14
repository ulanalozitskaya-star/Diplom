# Лозицкая Ульяна, 34-я когорта - Финальный проект. Инженер потестированию плюс

import requests
import configuration
import data

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
           json=data.order_body)

def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
           params={"t": track_number})

def get_track_number_of_order(order_body):
    track_number = post_new_order(order_body)
    return track_number.json()["track"]

def test_track_order():
    track_number = get_track_number_of_order(data.order_body)
    get_response = get_order_info(track_number)
    assert get_response.status_code == 200