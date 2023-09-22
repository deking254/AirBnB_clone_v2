#!/usr/bin/python3
"""this program is aimed to..."""
from flask.app import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """this is the function that prints hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """this is the function that prints hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """this is the function that prints hbnb"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    """this is the function that prints hbnb"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """this is the function that prints hbnb"""
    return str(n) + " is a number"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
