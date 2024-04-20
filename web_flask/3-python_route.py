#!/usr/bin/python3
"""Python web framework module - 0-hello_route"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Hello function binding the url to the route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Hello function binding the url to the route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """text display route"""
    text = text.replace("_", " ")
    return "C {}".format(escape(text))


@app.route("/python/<text>", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """Route displays python and text"""
    text = text.replace("_", " ")
    return "Python {}".format(escape(text))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
