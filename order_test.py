# Лозицкая Ульяна, 34-я когорта - Финальный проект. Инженер потестированию плюс

import requests
import configuration
import data
from sender_stand_request import post_new_order, get_order_info


def get_track_number_of_order():
    track_number = post_new_order()
    return track_number.json()["track"]

def test_track_order():
    track_number = get_track_number_of_order()
    get_response = get_order_info(track_number)
    assert get_response.status_code == 200

