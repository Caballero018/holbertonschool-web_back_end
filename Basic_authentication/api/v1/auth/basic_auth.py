#!/usr/bin/env python3
"""
Module has a class llamed BasicAuth
"""
from api.v1.auth.auth import Auth
from codecs import decode
import base64


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
    
    def decode_base64_authorization_header(self, base64_authorization_header: str)\
            -> str:
        """
        Method that returns the decoded value of a Base64 string
        'base64_authorization_header'
        """
        try:
            if not base64_authorization_header or type(base64_authorization_header) is not str:
                return None
            base = base64_authorization_header.encode()
            base = base64.b64decode(base)
            return decode(base, 'utf-8', 'strict')
        except base64.binascii.Error:
            return None
