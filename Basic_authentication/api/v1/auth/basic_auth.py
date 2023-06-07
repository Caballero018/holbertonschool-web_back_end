#!/usr/bin/env python3
"""
Doc
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Doc """
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if not base64_authorization_header or type(base64_authorization_header) is not str:
            return None
