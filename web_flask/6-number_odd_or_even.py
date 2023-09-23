#!/usr/bin/python3
"""this program is aimed to..."""
from flask.app import Flask
from flask import render_template_string, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """this is the function that prints hbnb"""
    d = '<!DOCTYPE html>\n<HTML lang="en">\n\t<HEAD>\n\t\t'
    b = '<TITLE>HBNB</TITLE>\n\t</HEAD>\n\t<BODY>\n\t\t'
    nu = '<H1>Number: {}</H1>\n\t</BODY>\n</HTML>'.format(n)
    s = d + b + nu
    return render_template_string(s, n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """this is the function that prints hbnb"""
    if n % 2 == 0:
        typ = 'is even'
    else:
        typ = 'is odd'
    return render_template('6-number_odd_or_even.html', n=n, typ=typ)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
