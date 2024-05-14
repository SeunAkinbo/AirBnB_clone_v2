#!/usr/bin/python3
"""Python web framework module - 0-hello_route"""
from flask import Flask
import socket

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Hello function binding the url to the route"""
    return "Hello HBNB!"

@app.route("/airbnb-onepage", strict_slashes=False)
def start():
    """Serving content on route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
