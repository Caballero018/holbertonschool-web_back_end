#!/usr/bin/env python3
"""
Class SessionAuth that inherits from Auth.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Methods (create_session and user_id_for_session_id) for storing and
    retrieving a link between a User ID and a Session ID.
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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Method that returns a User ID based on a Session ID.
        """
        if not session_id or not isinstance(session_id, str):
            return None
        user_value = SessionAuth.user_id_by_session_id.get(session_id)
        return user_value
