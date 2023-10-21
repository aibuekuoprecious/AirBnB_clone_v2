#!/usr/bin/python3

"""A script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


# Define a route for the root URL
@app.route("/", strict_slashes=False)
def display_hello():
    """Returns a simple greeting."""
    return "Hello HBNB!"


# Define a route for the /hbnb URL
@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Returns a simple greeting."""
    return "HBNB"


# Define a route for the /c/<text> URL
@app.route("/c/<text>", strict_slashes=False)
def display_cText(text):
    """Returns a greeting with the given text."""
    text = text.replace("_", " ")
    return "C %s" % (text)


# Define a route for the /python/ URL and the /python/<text> URL
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_pythonText(text='is cool'):
    """Function called with /python/<text> route"""
    if text != 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % (text)


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
