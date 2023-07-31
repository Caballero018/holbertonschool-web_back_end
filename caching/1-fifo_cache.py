#!/usr/bin/env python3
"""
Module that have a class FIFOCache that inherits from BaseCaching and is
caching system.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class FIFOCache that inherits from BaseCaching and is caching system.
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
