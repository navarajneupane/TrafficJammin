from settings import google_api_key
import datetime
import requests
import json
import time


def get_google(URL):
    response = requests.get(URL)

    if response.status_code == 200:
        return json.loads(response.content)
    else:
        raise ValueError('Google API request status code is not 200')


def request_arrival(org, dest, arr):
    '''Function that takes parsed request as an input
    and builds a list of requests to fire at Google api
    '''

    URL = 'https://maps.googleapis.com/maps/api/directions/json?' + \
          'origin={org}}&destination={dst}}&arrival_time={arr}}' + \
          '&key={google_api_key}&traffic_mode=pessimistic'.format(org=org,
                                                                  dst=dst,
                                                                  arr=arr,
                                                                  google_api_key=google_api_key)
    return get_google(URL)


def request_departure(org, dest, dep):
    '''Function that takes parsed request as an input
    and builds a list of requests to fire at Google api
    '''

    URL = 'https://maps.googleapis.com/maps/api/directions/json?' + \
          'origin={org}}&destination={dst}}&departure_time={arr}}' + \
          '&key={google_api_key}&traffic_mode=pessimistic'.format(org=org,
                                                                  dst=dst,
                                                                  arr=arr,
                                                                  google_api_key=google_api_key)
    return get_google(URL)


def get_duration(json_data):
    '''Function that parses API response from Google.

    Returns None for duration_in_traffic if this is not in json_data
    '''
    duration = json_data['routes'][0]['legs'][0]['duration']['value']//3600

    if 'duration_in_traffic' in json_data.keys():
        duration_in_traffic = json_data['routes'][0]['legs'][0]['duration_in_traffic']['value']/3600
    else:
        duration_in_traffic = None

    return duration, duration_in_traffic
