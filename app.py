from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return '<h1>Hello man, get it?</h1>'
