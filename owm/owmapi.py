# OpenWeatherMap API interface

import json
import requests

class OWM(object):
    DEFAULT_ENDPOINT = 'https://api.openweathermap.org'
    
    def __init__(self, apikey, units='metric'):
        self.apikey = apikey
        self.units = units
        pass

    def get_current_by_city(self, city_name, city_state=None, city_country=None, units=None):
        query_str = city_name
        if city_state:
            query_str += f",{city_state}"
        if city_country:
            query_str += f",{city_country}"

        if not units:
            units = self.units
        params = {
            'q': query_str,
            'appid': self.apikey,
            'units': units
        }
        r = requests.get(f"{self.DEFAULT_ENDPOINT}/data/2.5/weather", params=params)
#        print(f"r: {r.status_code}")
#        if r.status_code != 200:
#            print(f"Error: ({r.status_code}) {r.reason}")
#            return json.dumps({'status': r.status_code, 'message': r.reason})
#        else:
        return r.json()

    
    def get_current_by_geo(self, lat, lon, units=None):
        if not units:
            units = self.units
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.apikey,
            'units': units
        }
        r = requests.get(f"{self.DEFAULT_ENDPOINT}/data/2.5/weather", params=params)
        if r.status_code != 200:
            print(f"Error: ({r.status_code}) {r.reason}")
            return json.dumps({'status': r.status_code, 'message': r.reason})
        else:
            return r.json()


    def fail_current_by_geo(self, lat, lon, units=None):
        # this should fail because we do not supply the apikey
        if not units:
            units = self.units
        params = {
            'lat': lat,
            'lon': lon,
            'units': units
        }
        r = requests.get(f"{self.DEFAULT_ENDPOINT}/data/2.5/weather", params=params)
        if r.status_code != 200:
            print(f"Error: ({r.status_code}) {r.reason}")
            return json.dumps({'status': r.status_code, 'message': r.reason})
        else:
            return r.json()


    def never_called(self):
        return "foo"

