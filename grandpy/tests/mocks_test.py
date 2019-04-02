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