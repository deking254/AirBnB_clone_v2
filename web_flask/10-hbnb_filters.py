#!/usr/bin/python3
"""this program is aimed to..."""
from flask.app import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """this is the function that prints hello"""
    states = storage.all()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
