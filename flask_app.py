from flask import Flask, request, Response
from flask.ext.cors import CORS, cross_origin
from os import environ
import json
import time
import datetime
from engine import some_function_that_wraps_everything

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/api/fastRoute": {"origins": "http://localhost:5555"}})


def parse_input(json_data):
    # Parse arrival time
    arr = json_data['arr']
    arr = datetime.datetime(2017, 3, 20, int(arr[:2]), int(arr[-2:]))
    arr = int(time.mktime(arr.timetuple()))
    json_data['arr'] = arr

    return json_data


@app.route('/api/fastRoute', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def find_fastest_route():
    '''json_in = {"arr": "09:00",
                    "org": "Eindhoven",
                    "dst": "Veldhoven",
                    "tolerance": [15],
                    "active_days": [true, true, true, true, true, false, false]}
    '''
    input_json = request.get_json(force=True)

    # Parse input
    json_data = parse_input(input_json)

    # DO THE MAGIC
    output = some_function_that_wraps_everything(json_data)

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
