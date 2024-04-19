#!/usr/bin/python3
"""starts a Flask web application, C is fun!"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def python_text(text=None):
    if text is None:
        txt = 'is cool'
    else:
        txt = text.replace('_', ' ')
    return 'Python ' + txt


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
