#!/usr/bin/env python3
"""
Auth file
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """
    method that takes in a password string arguments and returns bytes.

    The returned bytes is a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    # password to encode in bytes
    password_encoded = password.encode()

    # generates random salt
    salt = bcrypt.gensalt()

    # hash the password with salt
    hashed_password = bcrypt.hashpw(password_encoded, salt)

    return hashed_password


def _generate_uuid() -> str:
    """ function that returns a string representation of a new uuid4 """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ method to register a user """
        try:
            # try to find user by email
            user = self._db.find_user_by(email=email)

        except NoResultFound:
            # if none user is found, create add the user
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        else:
            # if user is already registered, raise value error
            raise ValueError("User {} already exists.".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ valid login method """
        try:
            # try to locate user by email
            user = self._db.find_user_by(email=email)

            if user is not None:
                # if user exists check password, convert password to bytes
                hashed_password = password.encode('utf-8')

                # check password with bcrypt
                pwd = bcrypt.checkpw(hashed_password, user.hashed_password)

                return pwd

        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """
        The method should find the user corresponding to the email,
        generate a new UUID and store it in the database as the user’s
        session_id, then return the session ID.
        """
        try:
            # find the user corresponding to the email
            user = self._db.find_user_by(email=email)
            # generate a new UUID
            session_id = _generate_uuid()
            # store it in the database as the user’s session_id
            self._db.update_user(user.id, session_id=session_id)
            return session_id

        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User or None:
        """ get_user_from_session_id method. It takes a single session_id
        string argument and returns the corresponding User or None.
        If the session ID is None or no user is found, return None. Otherwise
        return the corresponding user.
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user

        except NoResultFound:
            return None

    def destroy_session(self, user_id) -> None:
        """ destroy_session method."""

        if user_id is None:
            return None

        try:
            # find the by id
            user = self._db.find_user_by(id=user_id)

            if user is not None:
                # update corresponding user's session ID to none
                self._db.update_user(user.id, session_id=None)

        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """  method to reset the password token """
        try:
            # Find the user corresponding to the email
            user = self._db.find_user_by(email=email)
            # generate a new uuid
            new_uuid = _generate_uuid()
            # update user's reset_token database field
            self._db.update_user(user.id, reset_token=new_uuid)
            return new_uuid
        except NoResultFound:
            raise ValueError("User DNE")

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update the password method """
        try:
            # find the user corresponding to the reset_token
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(
                user.id, hashed_password=hashed_password, reset_token=None)

        except NoResultFound:
            raise ValueError
