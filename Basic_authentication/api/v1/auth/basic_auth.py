#!/usr/bin/env python3
"""
Module has a class llamed BasicAuth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class BasicAuth that inherits from Auth """
    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """
        Method that returns the Base64 part of the Authorization header for a
        Basic Authentication
        """
        if not authorization_header or type(authorization_header) is not str\
                or "Basic " not in authorization_header[:6]:
            return None
        return authorization_header[6:]
