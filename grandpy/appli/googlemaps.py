import requests
from config import API_GOOGLE_MAP_KEY, GEOCODE_URL

address = '89 rue Carnot 62950 Noyelles-Godault'

def api_request(input_address):

    criteria_api = {
        'address': input_address,
        'country' : 'FR',
        'key' : API_GOOGLE_MAP_KEY
    }

    try:
        req = requests.get(GEOCODE_URL, params=criteria_api)
        res = req.json()

    except:
        print("Impossible de se connecter à l'API")

    try:
        latitude = res['results'][0]['geometry']['location']['lat']
        longitude = res['results'][0]['geometry']['location']['lng']
        #print("latitude: " + str(latitude) + " longitude: " + str(longitude))
        #coordinates = str(latitude) + '|' + str(longitude)
        return latitude, longitude

    except:
        print("Informations non trouvées")


