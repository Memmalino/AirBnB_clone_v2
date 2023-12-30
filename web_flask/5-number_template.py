#!/usr/bin/python3

"""
Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:                    Display "Hello HBNB!"
            /hbnb:                Display "HBNB"
            /c/<text>:            Display "C" + text (replace "_" with " ")
            /python/<text>:       Display "Python" + text (default="is cool")
            /number/<n>:          Display "n is a number" only if int
            /number_template/<n>: Display HTML page only if n is int
"""

from flask import Flask, render_template
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


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Displays 'Python' followed by the value of <text>.
    first route statement ensures it works for:
    curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
    curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Display html page only if int given
       place given int into html template
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
