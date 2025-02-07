#!/usr/bin/python3
"""this program is aimed to..."""
import os
from flask.app import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_bystate():
    """this is the function that prints hello"""
    states = storage.all("State")
    print(states)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
