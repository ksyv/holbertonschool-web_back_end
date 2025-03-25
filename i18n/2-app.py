#!/usr/bin/env python3
"""Modul for initialise flask with babel for en and fr"""
from flask import Flask, render_template, request
from flask_babel import Babel


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config:
    """"to config different languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def renderIndex():
    """This is the function index"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
