import requests

URL = "https://fr.wikipedia.org/w/api.php"

SEARCHPAGE = "89 rue Carnot 62950 Noyelles-Godault"

criteria_api = {
    'action':"query",
    'list' : "geosearch",
    'gscoord': '50.4238559|2.9977904',
    'gsradius': '10000',
    'gslimit' : '1',
    'format':"json"
}

criteria_api1 = {
    'action':"query",
    'pageids': '534775',
    'prop': 'extracts',
    'explaintext': 'true',
    'exintro': 'exintro',
    'exsentences': '3',
    'format':"json"
}

req = requests.get(URL, params=criteria_api1)
res = req.json()
#pageId = res['query']['geosearch'][0]['pageid']

print(res)