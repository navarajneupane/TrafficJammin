from flask import Flask, request, Response
from os import environ
import json
from some_script import functions

app = Flask(__name__)
app.debug = True

@app.route('/api/fastRoute', methods=['POST'])
def find_fastest_route():
    input_json = request.get_json(force=True)

    # Parse input

    # Feed to function that returns options

    # Parse for output
    output = {}

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
