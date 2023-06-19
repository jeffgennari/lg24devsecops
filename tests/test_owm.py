import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
import sys
import os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(cwd, '..'))
import owm

key = 'keymaterial'

def test_class():
    owmapi = owm.OWM(key)
    assert owmapi != None


@patch('owm.owmapi.requests')
def test_get_current_by_city(mock_requests):
    mock_response_obj = MagicMock()
    mock_response_obj.text = 'mock text'
    mock_response_obj.json = lambda: {"testkey": "testvalue"}
    mock_response_obj.status_code = 200
    mock_requests.get.return_value = mock_response_obj

    owmapi = owm.OWM(key)
    r = owmapi.get_current_by_city('Pittsburgh', 'PA', 'USA')
    assert r == {"testkey": "testvalue"}
    

@patch('owm.owmapi.requests')
def test_get_current_by_geo(mock_requests):
    mock_response_obj = MagicMock()
    mock_response_obj.text = 'mock text'
    mock_response_obj.json = lambda: {"testkey": "testvalue"}
    mock_response_obj.status_code = 200
    mock_requests.get.return_value = mock_response_obj

    owmapi = owm.OWM(key)
    lat = 40.4570944655325
    lon = -79.46340866622046
    r = owmapi.get_current_by_geo(lat, lon)
    assert r == {"testkey": "testvalue"}


