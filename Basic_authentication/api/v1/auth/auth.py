#!/usr/bin/env python3
"""modul for manage authentication
"""
from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    """class for manage authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Return: False if the path is in the list of strings excluded_paths
                True in oters cases
        """
        if path is None or excluded_paths is None or len(excluded_paths) < 1:
            return (True)
        if path[-1] != '/':
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                base_path = excluded_path[:-1]  # Remove the '*'
                if path.startswith(base_path):
                    return False
            elif path == excluded_path:
                return False

    def authorization_header(self, request=None) -> str:
        """
        Return: Value of Autorization request
                None if no Autorization in the header request.
        """
        if request is None or 'Authorization' not in request.headers:
            return (None)
        return (request.headers.get('Authorization'))

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return: None
        """
        return (None)
