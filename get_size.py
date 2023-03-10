import requests


def get_size_obj(address: str):
    toponym_to_find = address

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
    # Размеры топонима:
    toponym_spn = toponym["boundedBy"]["Envelope"]
    # Долгота и широта:
    # Максимальная и минимальная широта и долгота:
    max_coord = toponym_spn['upperCorner'].split()
    min_coord = toponym_spn['lowerCorner'].split()
    delta = [str((float(max_coord[0]) - float(min_coord[0]))), str((float(max_coord[1]) - float(min_coord[1])))]
    return delta