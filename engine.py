from settings import google_api_key
import datetime
import requests
import json
import time
import operator


def get_google(URL):
    response = requests.get(URL)

    if response.status_code == 200:
        return json.loads(response.content)
    else:
        print(json.loads(response.content))
        raise ValueError('Google API request status code is not 200')


def request_arrival(org, dst, arr):
    '''Function that takes parsed request as an input
    and builds a list of requests to fire at Google api
    '''

    URL = 'https://maps.googleapis.com/maps/api/directions/json?' + \
          'origin={org}&destination={dst}&arrival_time={arr}' + \
          '&key={google_api_key}'.format(org=org,
                                          dst=dst,
                                          arr=arr,
                                          google_api_key=google_api_key)
    return get_google(URL)


def request_departure(org, dst, dep):
    '''Function that takes parsed request as an input
    and builds a list of requests to fire at Google api
    '''

    print(dep)

    URL = 'https://maps.googleapis.com/maps/api/directions/json?origin={org}&destination={dst}&departure_time={dep}&key={google_api_key}&traffic_mode=pessimistic'.format(org=org, dst=dst, dep=dep,google_api_key=google_api_key)

    print URL
    return get_google(URL)


def get_departure_duration_times(json_data, base_duration):
    org = json_data['org']
    dst = json_data['dst']
    arr = json_data['arr']
    tolerance_time = json_data['tolerance']

    departure_times = []
    best_departure_time = arr - base_duration
    departure_times = [best_departure_time]

    tolerance_factor = tolerance_time/10

    for t in range(0, tolerance_factor):
        departure_times.append(best_departure_time - (t+1)*10*60)
        departure_times.append(best_departure_time + (t+1)*10*60)

    departure_and_duration = {}
    for d in range(0, len(departure_times)):
        json_data = request_departure(org, dst, departure_times[d])
        departure_and_duration[departure_times[d]] = get_duration_in_traffic(json_data)

    return departure_and_duration


def get_min_travel_time(departure_and_duration):
    sorted_dict = sorted(departure_and_duration.iteritems(), key=operator.itemgetter(1))  # Sort dictionary based on values
    return sorted_dict[0]


def get_duration(org, dst, arr):
    google_response = request_arrival(org, dst, arr)
    duration = google_response['routes'][0]['legs'][0]['duration']['value']

    return duration


def get_duration_in_traffic(json_data):
    return json_data['routes'][0]['legs'][0]['duration_in_traffic']['value']


def parse_input_json(json_data):
    arr = json_data['arr']
    org = json_data['org']
    dst = json_data['dst']
    tolerance = json_data['tolerance']

    return arr, org, dst, tolerance


def some_function_that_wraps_everything(json_data):
    # Parse JSON data
    arr, org, dst, tolerance = parse_input_json(json_data)

    # Get base duration
    base_duration = get_duration(org, dst, arr)

    # Get list of departure times
    departure_and_duration = get_departure_duration_times(json_data, base_duration)

    # Get minimum departure time
    min_travel_time = get_min_travel_time(departure_and_duration)
