#!/usr/bin/python3
"""this program is aimed to..."""
from flask.app import Flask;
app = Flask(__name__);
@app.route("/")
def index():
    """this is the function that prints hello"""
        return "Hello HBNB!";
app.run(host="0.0.0.0", port="5000");
