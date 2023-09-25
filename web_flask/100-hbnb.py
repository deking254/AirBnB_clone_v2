#!/usr/bin/python3
"""this program is aimed to..."""
from flask.app import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def states():
    """this is the function that prints hello"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    users = storage.all('User')
    return render_template("100-hbnb.html", users=users, states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
