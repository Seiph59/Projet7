import requests
import config

def request_api_google(input_address):

    criteria_api = {
        'address': input_address,
        'country' : 'FR',
        'key' : API_GOOGLE_MAP_KEY
    }

    req = requests.get(GEOCODE_URL, params=criteria_api)
    res = req.json()

    latitude = res['results'][0]['geometry']['location']['lat']
    longitude = res['results'][0]['geometry']['location']['lng']

    #print("latitude: " + str(latitude) + " longitude: " + str(longitude))
    return latitude, longitude

""" address = '89 rue Carnot 62950 Noyelles-Godault'
test = request_api_google(address)
print(test[0], test[1]) """