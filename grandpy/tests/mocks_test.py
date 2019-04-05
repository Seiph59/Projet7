import requests
import json

from ..appli import googlemaps
from ..appli import api_wikisearch


address = '89 rue Carnot 62950 Noyelles-Godault'
coordinates = '50.4238559|2.9977904'
page_id = 534775

def test_request_google(monkeypatch):
    result = [50.4238559, 2.9977904]
    response = {
        'results':[{
            "geometry":{
                "location":{
                    "lat": 50.4238559,
                    "lng": 2.9977904
                }
            }
        }]
    }

    def mock_get(requests, params):
        class FakeResponse:
            def raise_for_status(self):
                return
            def json(self):
                return response
        return FakeResponse()

    monkeypatch.setattr('requests.get', mock_get)
    request_lat, request_lng = googlemaps.get_coords_from_address(address)
    assert request_lat == result[0]
    assert request_lng == result[1]


def test_request_pageid_wikimedia(monkeypatch):
    result = 534775
    response = {
        'query':{
            'geosearch':[{
                'pageid': 534775
                }]
            }
        }

    def mock_get_wiki(requests, params):
        class FakeResponse:
            def json(self):
                return response
        return FakeResponse()

    monkeypatch.setattr('requests.get', mock_get_wiki)
    request_pageid = api_wikisearch.search_coordinates(coordinates)
    assert request_pageid == result


def test_request_page_content_wiki(monkeypatch):
    result = ["https://fr.wikipedia.org/wiki/Noyelles-Godault",
    "Noyelles-Godault est une commune française située dans le département du Pas-de-Calais en région Hauts-de-France. Ses habitants sont appelés les Noyellois."]
    response = {
        'query':{
            'pages':{
                '534775':{
                    'fullurl':'https://fr.wikipedia.org/wiki/Noyelles-Godault',
                    'extract':'Noyelles-Godault est une commune française située dans le département du Pas-de-Calais en région Hauts-de-France. Ses habitants sont appelés les Noyellois.'
                }
            }
        }
    }
    def mock_get_wiki2(requests, params):
        class FakeResponse2:
            def json(self):
                return response
        return FakeResponse2()

    monkeypatch.setattr('requests.get', mock_get_wiki2)
    request_url, request_extract = api_wikisearch.search_page_content(page_id)
    assert request_extract == result[0]
    assert request_url == result[1]
