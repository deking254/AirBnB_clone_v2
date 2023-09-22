#!/usr/bin/python3
"""this program is aimed to..."""
from flask.app import Flask;
app = Flask(__name__);
print((app.default_config));
@app.route("/")
def index():
        return "Hello HBNB!";
app.run(host="0.0.0.0", port="5000");
