"""
File who manage the differents interactions with the API Wikipedia
"""

import requests

URL = "https://fr.wikipedia.org/w/api.php"


class WikiException(Exception):
    """
    Class used to generate a specific error_message.
    """


def search_coordinates(coordinates_input):
    """
    Method who received the coordinates from Flask, and return the page id
    """
    criteria_api = {
        'action': "query",
        'list': "geosearch",
        'gscoord': coordinates_input,
        'gsradius': '10000',
        'gslimit': '1',
        'format': "json"
    }
    try:
        req = requests.get(URL, params=criteria_api)
        res = req.json()
        id_page = res['query']['geosearch'][0]['pageid']
        return id_page

    except requests.exceptions.Timeout as out:
        print("Timeout Error: ", out)


def search_page_content(input_id):
    """
    Receive Page id to receive the page content associated
    """
    criteria_research = {
        'action': "query",
        'pageids': input_id,
        'prop': 'info|extracts',
        'inprop': 'url',
        'explaintext': 'true',
        'exsentences': 2,
        'format': "json"
        }
    try:
        req = requests.get(URL, params=criteria_research)
        res = req.json()
        url_page = res['query']['pages'][str(input_id)]['fullurl']
        intro_sentences = res['query']['pages'][str(input_id)]['extract']
        print(intro_sentences, url_page)
        return intro_sentences, url_page

    except KeyError:
        print("Informations non trouvées")


def research_page(coordinates_list):
    """
    Intermediary method allowing to execute both requests above
    with that one.
    """
    lat = coordinates_list[0]
    lng = coordinates_list[1]
    coordinates_formated = str(lat) + '|' + str(lng)
    page_id = search_coordinates(coordinates_formated)
    page_content_list = search_page_content(page_id)
    return page_content_list
