#!/usr/bin/env python3
"""
Doc
"""
from flask import request
from typing import List, TypeVar


def remove_slash(string: str) -> str:
    """
    Funtion that removes forward slash
    """
    if string[-1] == '/':
        string = string[:-1]
    return string


class Auth():
    """ Doc """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Doc """
        if not path:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        excluded_paths = [remove_slash(paths) for paths in excluded_paths]
        if remove_slash(path) not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ Doc """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Doc """
        return None
