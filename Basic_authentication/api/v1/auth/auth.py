#!/usr/bin/env python3 
"""modul for manage authentication
"""
from flask import request 
from typing import List, TypeVar


class Auth:
    """class for manage authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Return: False
        """
        return (False)
    
    def authorization_header(self, request=None) -> str:
        """
        Return: None
        """
        return (None)
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return: None
        """
        return (None)
