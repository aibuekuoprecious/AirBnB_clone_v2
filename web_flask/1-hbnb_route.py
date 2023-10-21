#!/usr/bin/python3

"""A script that starts a Flask web application"""

# Import the Flask library
from flask import Flask

# Create a Flask app
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


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
