#!/usr/bin/env python3
"""
Modulo that has a module a class called Cache
"""
import redis
import uuid
from typing import Union


class Cache():
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method store

        Keyword arguments:
        data -- Data that is set in the object
        Return: return_description
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
    
    def get(self, key, fn):
        if self._redis.get(key) == None:
            return None
        value = self._redis.get(key)
        return value

    def get_str(self, value):
        if type(value) == str:
            return str(value)

    def get_int(self, value):
        if type(value) == int:
            return int(value)
