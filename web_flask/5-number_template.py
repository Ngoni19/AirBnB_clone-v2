#!/usr/bin/python3
"""
The script starts Flask web application
    listen on 0.0.0.0, port 5000
    routes: /:                    display "Hello HBNB!"
            /hbnb:                display "HBNB"
            /c/<text>:            display "C" + text (replace "_" with " ")
            /python/<text>:       display "Python" + text (default="is cool")
            /number/<n>:          display "n is a number" only if int
            /number_template/<n>: display HTML page only if n is int
"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def helloo_hbnb():
    """Display the  text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def custom_text(text):
    """Display custom text: """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Display custom text: """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def txt_if_int(n):
    """Display text only if int is given"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def html_if_int(n):
    """Display html pages only if int is given"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
