import requests
import json

from ..appli import googlemaps


address = '89 rue Carnot 62950 Noyelles-Godault'


"""
class MockRequestGet:

    def __init__(self, url, params=None):
        pass
"""
def test_request_google(monkeypatch):
    result = [50.4238559, 2.9977904]
    response = {
        'results':[{
            "lat ": 50.4238559,
            "lng": 2.9977904
        }]
        }

    def mock_get(requests, params):
        return response

    monkeypatch.setattr('requests.get', mock_get)
    assert len(googlemaps.api_request(address)) == len(result)