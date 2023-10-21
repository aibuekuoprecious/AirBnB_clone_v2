#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """After each request, remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page (inside the tag BODY) with a list of all states."""
    states_lst = storage.all(State)
    return render_template("9-states.html", states_lst=states_lst)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """Displays a HTML page (inside the tag BODY) with a single state."""
    state = storage.get(State, id)
    return render_template("9-states.html", state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

