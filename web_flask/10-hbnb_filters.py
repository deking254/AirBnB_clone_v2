#!/usr/bin/python3
"""this program is aimed to..."""
from flask.app import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """this is the function that prints hello"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
