#!/usr/bin/python3

"""
    This Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:         Display "Hello HBNB!"
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Displays 'C' followed by the value of <text>."""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)