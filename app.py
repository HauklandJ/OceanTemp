from flask import Flask, jsonify, request
from measurement import Measurement

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return '<h1>Hello man, get it?</h1>'


@app.route('/api/temps/', methods=['GET'])
def temps():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id provided."
    result = 0

    for temp in tempsDict:
        if temp['id'] == id:
            result = temp
    return jsonify(result)


tempsDict = [
    {'id': 0,
     'temp': 18.154,
     'time': '2020-07-02 08:05:23.283'
     },
    {'id': 1,
     'temp': 18.231,
     'time': '2020-07-02 10:05:23.283'
     },
    {'id': 2,
     'temp': 18.193,
     'time': '2020-07-02 12:05:23.283'
     }
]
