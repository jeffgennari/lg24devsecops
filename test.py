#!/usr/bin/env python3
# Note that this requires a valid OpenWeatherMap API key in one of
# the following locations:
#   envvar APIKEY
#   local file .apikey
#   $HOME/.apikey

import os
import sys
import owm

apikey = None
if 'APIKEY' in os.environ:
    apikey = os.environ['APIKEY']
elif os.path.isfile('.apikey'):
    with open('.apikey', 'r') as keyfile:
        apikey = keyfile.read().strip()
elif 'HOME' in os.environ and os.path.isfile(os.path.join(os.environ['HOME'], '.apikey')):
    with open(os.path.join(os.environ['HOME'], '.apikey'), 'r') as keyfile:
        apikey = keyfile.read().strip()
else:
    print("OWM API key env/keyfile not found! Exiting!")
    sys.exit(-1)

owmapi = owm.OWM(apikey)

r = owmapi.get_current_by_city('Pittsburgh', 'PA', 'USA')
print(r)

lat = 40.5570944655325
lon = -79.76340866622046
r = owmapi.get_current_by_geo(lat, lon)
print(r)

r = owmapi.fail_current_by_geo(lat, lon)
print(r)
