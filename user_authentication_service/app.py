#!/usr/bin/env python3
"""
App file
"""
from flask import Flask, jsonify, abort, request, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def payload():
    """ payload function"""
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    implement the end-point to register a user. Define a users function
    that implements the POST /users route.
    """
    # get the data from the form
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        # try to register
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        # if the user already exists
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    login function to respond to the POST /sessions route.

The request is expected to contain form data with "email" and a "password"
fields.

If the login information is incorrect, use flask.abort to respond with a
401 HTTP status.

Otherwise, create a new session for the user, store it the session ID as a
cookie with key "session_id" on the response and return a JSON payload of
the form
    """
    # get email and password
    email = request.form.get('email')
    password = request.form.get('password')

    # check login informations
    if AUTH.valid_login(email, password):
        # create session for user and generate a new id
        session_id = AUTH.create_session(email=email)
        response = jsonify({"email": email, "message": "logged in"})
        # store session id inasmuch as cookie
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """
    logout function to respond to the DELETE /sessions route.
    The request is expected to contain the session ID as a cookie with key
    "session_id".

    Find the user with the requested session ID. If the user exists destroy
    the session and redirect the user to GET /. If the user does not exist,
    respond with a 403 HTTP status.
    """
    # get the sessionID as cookie with request
    session_id_cookie = request.cookies.get('session_id')

    # Find the user with the requested session ID
    user = AUTH.get_user_from_session_id(session_id_cookie)
    # if the user exists, destroy session and redirect to GET /
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/', code=302)
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ Profile function """
    # get the sessionID as cookie with request
    session_id_cookie = request.cookies.get('session_id')

    # find user by session ID
    user = AUTH.get_user_from_session_id(session_id_cookie)

    if user:
        return jsonify({"email": user.email}), 200

    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """
    function to respond to the POST /reset_password route.
    The request is expected to contain form data with the "email" field.

    If the email is not registered, respond with a 403 status code. Otherwise,
    generate a token and respond with a 200 HTTP status and the following
    JSON payload: {"email": "<user email>", "reset_token": "<reset token>"}
    """
    try:
        # contain form data with the "email" field.
        email = request.form.get('email')
        # generate a token
        token_generated = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token_generated}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """
    function in the app module to respond to the PUT /reset_password route.

    The request is expected to contain form data with fields "email",
    "reset_token" and "new_password".

    Update the password. If the token is invalid, catch the exception and
    respond with a 403 HTTP code.

    If the token is valid, respond with a 200 HTTP code and the following
    JSON payload:
    """
    # contain form data with fields "email", "reset_token", "new_password"
    email = request.form.get('email')
    new_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        # Update the password
        AUTH.update_password(new_token, new_password)
        msg = {"email": email, "message": "Password updated"}
        return jsonify(msg), 200

    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
