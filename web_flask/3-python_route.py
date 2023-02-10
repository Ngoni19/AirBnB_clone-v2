#!/usr/bin/python3
"""
The script starts Flask web application
    listening on 0.0.0.0, port 5000
    routes: /:              display "Hello HBNB!"
            /hbnb:          display "HBNB"
            /c/<text>:      display "C" + text (replace underscores with space)
            /python/<text>: display "Python" + text (default is "is cool")
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def helloo_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Display the text"""
    return "HBNB"


@app.route('/c/<text>')
def custom_text(text):
    """Display custom text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def pytho_text(text="is cool"):
    """display custom text given"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
