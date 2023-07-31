#!/usr/bin/env python3
"""
Module that have a class MRUCache that inherits from BaseCaching and is
caching system.
"""
from base_caching import BaseCaching
import collections


class MRUCache(BaseCaching):
    """
    Class MRUCache that inherits from BaseCaching and is caching system.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = collections.OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
            mru_key = [k for k in self.cache_data.keys()]
            self.cache_data.pop(mru_key[-2])
            print("DISCARD: {}".format(mru_key[-2]))

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
