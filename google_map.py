import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

def googleMap(place, w, h):
    URL = f'https://maps.googleapis.com/maps/api/staticmap?'
    PLACE = f'center={place}'
    SIZE = '&size=640x640&scale=2'
    KEY = '&key='

    MSG = URL + PLACE + SIZE + KEY

    # 구글로 요청
    resp = requests.get(MSG)

    img = QPixmap()
    img.loadFromData(resp.content)

    # resizing
    img = img.scaled(w, h, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

    return img