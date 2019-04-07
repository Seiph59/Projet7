"""
File used to request to Google's API
"""
import os
import requests
# from config import API_GOOGLE_MAP_KEY

GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

api_google_map_key = os.environ.get('API_GOOGLE_MAP_KEY')

class GoogleException(Exception):
    """
    Class used to generate a specific error_message.
    """


def get_coords_from_address(input_address):
    """
    Send an address to the google Geocode API, to receive coordinates
    """
    print(input_address)
    criteria_api = {
        'address': input_address,
        'country': 'FR',
        'key': api_google_map_key
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
