#!/usr/bin/env python3
"""modul for manage authentication
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class who extends the Auth class
    """
    pass
