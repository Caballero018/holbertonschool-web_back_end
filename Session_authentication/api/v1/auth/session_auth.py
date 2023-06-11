#!/usr/bin/env python3
"""
Class SessionAuth that inherits from Auth.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Doc
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Method that creates a Session ID for a user_id
        """
        if not user_id or not isinstance(user_id, str):
            return None
        id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[id] = user_id
        return id
