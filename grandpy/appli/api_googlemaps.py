import requests
from config import API_GOOGLE_MAP_KEY

geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"

criteria_api = {
    'address': '89 Rue Carnot, Noyelles-Godault',
    'country' : 'FR',
    'key' : API_GOOGLE_MAP_KEY

}
req = requests.get(geocode_url, params=criteria_api)
res = req.json()

latitude = res['results'][0]['geometry']['location']['lat']
longitude = res['results'][0]['geometry']['location']['lng']

print("latitude: " + str(latitude) + " longitude: " + str(longitude))