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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def intNumber(n):
    return ("{:d} is a number".format(n))


@app.route('/number_template/<n>', strict_slashes=False)
def numberTemplate():
    return <H1>'Number:  {:d}'.format(n)</H1>

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
