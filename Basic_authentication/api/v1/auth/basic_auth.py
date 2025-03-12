#!/usr/bin/env python3
"""modul for manage authentication
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class who extends the Auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return (None)
        if 'Basic' not in authorization_header:
            return (None)
        return authorization_header[6:]
