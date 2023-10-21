#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask
from flask import render_template

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

# Define a route for the /number/<int:n> URL


@app.route('/number/<int:n>', strict_slashes=False)
def display_if_int(n):
    """Returns a message if the input is an integer."""
    return '%d is a number' % (n)

# Define a route for the /number_template/<int:n> URL


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_render_num(n):
    """Renders a template with the given number."""
    return render_template('5-number.html', num=n)

# Define a route for the /number_odd_or_even/<int:n> URL


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_render_even_odd(n):
    """Renders a template with the given number, indicating whether it is odd or even."""
    return render_template('6-number_odd_or_even.html', num=n)


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
