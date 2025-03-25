#!/usr/bin/env python3
"""Modul for initialise flask with babel for en and fr"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """"to config different languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """to determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.context_processor
def inject_locale():
    """Injecte la fonction get_locale dans le contexte du template"""
    return dict(get_locale=get_locale)


@app.route('/')
def renderIndex():
    """This is the function index"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
