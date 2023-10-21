#!/usr/bin/python3
"""
Script starts Flask web app
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters", strict_slashes=False)
def html_filters():
    """Displays an HTML page with working city/state filters and amenities, running with web static CSS files."""

    state_objs = [s for s in storage.all("State").values()]
    amenity_objs = [a for a in storage.all("Amenity").values()]

    return render_template(
        "10-hbnb_filters.html",
        state_objs=state_objs,
        amenity_objs=amenity_objs,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
