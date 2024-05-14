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

def find_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()
    return port


if __name__ == "__main__":
    port = find_port()
    app.run(host='0.0.0.0', port=port, debug=True)
