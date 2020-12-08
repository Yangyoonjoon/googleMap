import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

def googleMap(place, w, h, z, t):
    URL = f'https://maps.googleapis.com/maps/api/staticmap?'
    PLACE = f'center={place}'
    SIZE = '&size=640x640&scale=2'
    # 키 필요
    KEY = '&key='
    ZOOM = f'&zoom={z}'
    TYPE = f'&maptype={t}'
    MARKER = f'&markers=color:0xFF0000|label:A|{place}'

    MSG = URL + PLACE + SIZE + ZOOM + TYPE + MARKER + KEY

    # 구글로 요청
    resp = requests.get(MSG)

    img = QPixmap()
    img.loadFromData(resp.content)

    # resizing
    img = img.scaled(w, h, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

    return img