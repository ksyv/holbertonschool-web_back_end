#!/usr/bin/env python3
"""modul for manage session authentication
"""
from flask import request
from typing import List, TypeVar
from models.user import User
from api.v1.auth.auth import Auth
import re


class SessionAuth(Auth):
    """class for manage session authentication
    """
    pass
