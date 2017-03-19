from flask import Flask, request, Response
from os import environ
import json
import time
import datetime

app = Flask(__name__)
app.debug = True


def parse_input(json_data):
    # Parse arrival time
    arr = json_data['arr']
    arr = datetime.datetime(2017, 3, 20, int(arr[:2]), int(arr[-2:]))
    arr = int(time.mktime(arr.timetuple()))
    json_data['arr'] = arr

    return json_data

@app.route('/api/fastRoute', methods=['POST'])
def find_fastest_route():
    input_json = request.get_json(force=True)
    '''json_in = {"arr": "09:00",
                    "org": "Eindhoven",
                    "dst": "Veldhoven",
                    "tolerance": [-38, 14],
                    "active_days": [true, true, true, true, true, false, false]}
    '''

    # Parse input
    json_data = parse_input(input_json)

    # Parse for output
    output = json_data

    # Return output
    return json.dumps(output)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = 5555
    except ValueError:
        PORT = 5555

    print "Started Jammin'!"
    app.run(HOST, PORT)
