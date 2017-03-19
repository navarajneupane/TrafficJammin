import requests
import json
from settings import google_api_key


def request_from_google(json_in, time_type='arr'):
    '''Function that takes parsed request as an input
    and builds a list of requests to fire at Google api
    '''
    org = json_in['org']
    dst = json_in['dst']
    time = json_in[time_type]

    URL = 'https://maps.googleapis.com/maps/api/directions/json?' + \
          'origin={org}}&destination={dst}}&{time_type}={time}}' + \
          '&key={google_api_key}'.format(org=org,
                                         dst=dst,
                                         time_type=time_type,
                                         time=time,
                                         google_api_key=google_api_key)

    response = requests.get(URL)

    if response.status_code = 200:
        return json.loads(response.content)
    else:
        raise ValueError('Google API request status code is not 200')


def get_duration(json_data):
    '''Function that parses API response from Google.

    Returns None for duration_in_traffic if this is not in json_data
    '''
    duration = json_data['routes'][0]['legs'][0]['duration']['value']

    if 'duration_in_traffic' in json_data.keys():
        duration_in_traffic = json_data['routes'][0]['legs'][0]['duration_in_traffic']['value']
    else:
        duration_in_traffic = None

    return duration, duration_in_traffic

# Function that collects responses from Google API

# Function that checks which is the shortest
