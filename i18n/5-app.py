#!/usr/bin/env python3
"""Modul for initialise flask with babel for en and fr"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """"to config different languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Return dict user if 'login_as', or None.
    """
    user_id_str = request.args.get('login_as')
    if user_id_str:
        try:
            user_id = int(user_id_str)
            return users.get(user_id)
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    """Find user (if get_user) and put in flask.g.user."""
    current_user = get_user()
    g.user = current_user


def get_locale():
    """to determine the best match with our supported languages"""
    locale_arg = request.args.get('locale')
    if locale_arg and locale_arg in app.config['LANGUAGES']:
        return locale_arg
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.context_processor
def inject_locale():
    """Injecte la fonction get_locale dans le contexte du template"""
    return dict(get_locale=get_locale)


@app.route('/')
def renderIndex():
    """This is the function index"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
