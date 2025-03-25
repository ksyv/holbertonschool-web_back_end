#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user to db """
        # create new user instance with email and password
        user = User(email=email, hashed_password=hashed_password)

        # add the user to the database
        self._session.add(user)

        # commit
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """
        method takes in arbitrary keyword arguments and returns the first
        row found in the users table as filtered by the method’s input
        arguments.
        """
        if kwargs is None:
            raise InvalidRequestError

        # query to filter the users that match with arguments
        query = self._session.query(User).filter_by(**kwargs)

        # store the first line
        first_row = query.first()

        if first_row is None:
            raise NoResultFound

        return first_row

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        method that takes as argument a required user_id integer and
        arbitrary keyword arguments, and returns None.

        The method will use find_user_by to locate the user to update, then
        will update the user’s attributes as passed in the method’s arguments
        then commit
        changes to the database.

        If an argument that does not correspond to a user attribute is passed,
        raise a ValueError.
        """
        # find user to update by id
        user_to_update = self.find_user_by(id=user_id)

        if user_to_update is None:
            raise ValueError

        # update the user with attributes kwargs
        for key, value in kwargs.items():
            if hasattr(user_to_update, key):
                # define attributes
                setattr(user_to_update, key, value)
            else:
                raise ValueError

        self._session.commit()

        return user_to_update
