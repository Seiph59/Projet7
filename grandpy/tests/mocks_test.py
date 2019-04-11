"""
File used to check if the method used for API requests works
"""
from ..appli import googlemaps
from ..appli import api_wikisearch


ADDRESS = '89 rue Carnot 62950 Noyelles-Godault'
COORDINATES = '50.4238559|2.9977904'
PAGE_ID = 534775


def test_request_google(monkeypatch):
    """
    Method who check if the method who send to the google api works
    """
    result = [50.4238559, 2.9977904]
    response = {
        'results': [{
            "geometry": {
                "location": {
                    "lat": 50.4238559,
                    "lng": 2.9977904
                }
            }
        }]
    }

    def mock_get(requests, params):
        class FakeResponse:
            """
            Mock the request from the 'get_coords_from_address' function
            """
            def raise_for_status(self):
                """
                Mock 'req.raise_for_status()', in the 'get_coord....' function
                """
                return

            def json(self):
                """
                Mock the response format Json, in the 'get_coord....' function
                """
                return response
        return FakeResponse()

    monkeypatch.setattr('requests.get', mock_get)
    request_lat, request_lng = googlemaps.get_coords_from_address(ADDRESS)
    assert request_lat == result[0]
    assert request_lng == result[1]


def test_request_pageid_wikimedia(monkeypatch):
    """
    Method who test the first API request for Wikimedia to receive a page id
    """
    result = 534775
    response = {
        'query': {
            'geosearch': [{
                'pageid': 534775
                }]
            }
        }

    def mock_get_wiki(requests, params):
        class FakeResponse:
            """
            Mock the 'search_coordinates()' function in api_wikisearch
            """
            def json(self):
                """
                Mock the response format Json, in the 'search_coo...' function
                """
                return response
        return FakeResponse()

    monkeypatch.setattr('requests.get', mock_get_wiki)
    request_pageid = api_wikisearch.search_coordinates(COORDINATES)
    assert request_pageid == result


def test_request_page_content_wiki(monkeypatch):
    """
    Method who test the second API request to get the page content requested
    """
    result = ["https://fr.wikipedia.org/wiki/Noyelles-Godault",
              "Noyelles-Godault est une commune française située dans le département du Pas-de-Calais en région Hauts-de-France. Ses habitants sont appelés les Noyellois."]
    response = {
        'query': {
            'pages': {
                '534775': {
                    'fullurl': 'https://fr.wikipedia.org/wiki/Noyelles-Godault',
                    'extract': 'Noyelles-Godault est une commune française située dans le département du Pas-de-Calais en région Hauts-de-France. Ses habitants sont appelés les Noyellois.'
                }
            }
        }
    }

    def mock_get_wiki2(requests, params):
        class FakeResponse2:
            """
            Mock the 'search_page_content()
            """
            def json(self):
                """
                Mock the response format Json, in the 'search_pag...' function
                """
                return response
        return FakeResponse2()

    monkeypatch.setattr('requests.get', mock_get_wiki2)
    request_url, request_extract = api_wikisearch.search_page_content(PAGE_ID)
    assert request_extract == result[0]
    assert request_url == result[1]
