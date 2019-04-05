import requests
from config import API_GOOGLE_MAP_KEY, GEOCODE_URL

address = '89 rue Carnot 62950 Noyelles-Godault'


class GoogleException(Exception):
    pass


def get_coords_from_address(input_address):
    print(input_address)
    criteria_api = {
        'address': input_address,
        'country': 'FR',
        'key': API_GOOGLE_MAP_KEY
    }

    try:
        req = requests.get(GEOCODE_URL, params=criteria_api)
        req.raise_for_status()
        res = req.json()

    except requests.exceptions.Timeout as out:
        print("Timeout Error: ", out)

    try:
        latitude = res['results'][0]['geometry']['location']['lat']
        longitude = res['results'][0]['geometry']['location']['lng']
        # print("latitude: " + str(latitude) + " longitude: " + str(longitude))
        # coordinates = str(latitude) + '|' + str(longitude)
        return latitude, longitude

    except KeyError:
        print("Informations non trouvées")
