#!/usr/bin/env python3
"""Task 3: API Authentication management"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required
        Returns True if the path is not in the list of strings excluded_paths.
        """

        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        path2 = path if path.endswith('/') else path + '/'
        for excluded_path in excluded_paths:
            if path == excluded_path or path2 == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header if present
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if not header:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user based on the request
        """
        return None
