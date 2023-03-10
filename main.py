import json
import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт
import requests
from PIL import Image
from get_size import get_size_obj


toponym_to_find = input('Введите адрес: ')

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    print('ОШИБКА response!')
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
# Собираем параметры для запроса к StaticMapsAPI:

map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join(get_size_obj(toponym_to_find)),
    "l": "map",
    'pt': ",".join([toponym_longitude, toponym_lattitude])
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)
print(response.url)
Image.open(BytesIO(
    response.content)).show()
