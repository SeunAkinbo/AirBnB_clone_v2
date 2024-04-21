#!/usr/bin/python3
"""Flask server for HBNB state"""

from flask import Flask, render_template
from models import *

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Renders the HTML, displaying states in a list of States"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_mysql_db():
    """Removes the current MYSQL session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
