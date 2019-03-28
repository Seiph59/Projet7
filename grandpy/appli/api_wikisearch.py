import requests

URL = "https://fr.wikipedia.org/w/api.php"

SEARCHPAGE = "6 place de l'étoile 75000 Paris"
coordinates = '50.4238559|2.9977904'

def search_coordinates (coordinates_input):
    criteria_api = {
        'action':"query",
        'list' : "geosearch",
        'gscoord': coordinates_input,
        'gsradius': '10000',
        'gslimit' : '1',
        'format':"json"
    }
    try:
        req = requests.get(URL, params=criteria_api)
        res = req.json()
        id_page = res['query']['geosearch'][0]['pageid']
        #print(id_page)
        return id_page

    except:
        return "Impossible de se connecter à l'api"

def search_page_content (input_id):
    PARAMS = {
    'action':"query",
    'pageids': input_id,
    'prop': 'info|extracts',
    'inprop': 'url',
    'explaintext': 'true',
    'exsentences': 2,
    'format':"json"
    }
    try:
        req = requests.get(URL, params=PARAMS)
        res = req.json()
        url_page = res['query']['pages'][str(input_id)]['fullurl']
        intro_sentences = res['query']['pages'][str(input_id)]['extract']
        return url_page, intro_sentences

    except:
        return "Désolé, je n'ai pas rien trouvé ..."

def research_page(coordinates_list):
    lat = coordinates_list[0]
    lng = coordinates_list[1]
    coordinates_formated = str(lat) + '|'+ str(lng)
    page_id = search_coordinates(coordinates_formated)
    page_content_list = search_page_content(page_id)
    return page_content_list
