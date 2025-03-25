#!/usr/bin/env python3
"""Modul for initialise flask"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def renderIndex():
    """This is the function index"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
