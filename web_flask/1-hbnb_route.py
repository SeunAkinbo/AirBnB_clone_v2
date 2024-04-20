#!/usr/bin/python3
"""Python web framework module - 0-hello_route"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""Hello function binding the url to the route"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
        """Hello function binding the url to the route"""
        return "HBNB"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)