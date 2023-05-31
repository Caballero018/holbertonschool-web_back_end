#!/usr/bin/env python3
"""
Module that have a class LRUCache that inherits from BaseCaching and is
caching system.
"""
from base_caching import BaseCaching
import collections


class LRUCache(BaseCaching):
    """
    Class LRUCache that inherits from BaseCaching and is caching system.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = collections.OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            lru_key = self.cache_data.move_to_end(key)
        if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data.keys()))
            self.cache_data.pop(lru_key)
            print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
