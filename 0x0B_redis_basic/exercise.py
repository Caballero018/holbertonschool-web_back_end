#!/usr/bin/env python3
"""
Modulo that has a module a class called Cache
"""
import redis
import uuid
from typing import Union, Optional


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

    def get(self, key: str, fn: Optional[callable] = None):
        """Method get

        Keyword arguments:
        key -- string argument
        fn  -- optional Callable argument
        Return: return_description
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Method get_str

        Keyword arguments:
        key -- string argument
        Return: conversion of data to str
        """
        return self.get(key, str)

    def get_int(self, key: int) -> int:
        """Method get_str

        Keyword arguments:
        key -- string argument
        Return: conversion of data to int
        """
        return self.get(key, int)
