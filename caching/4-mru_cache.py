#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """
        Initializes the Mru cache.
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """put an item to the cache.
        Args:
            key: The key for the item.
            item: The item to be added.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.key_order.remove(key)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop()
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self.key_order.append(key)

    def get(self, key):
        """
        Get an item from the cache.
        Args:
            key: The key of the item to be retrieved.
        Returns:
            The item if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None