#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def put(self, key, item):
        """put an item to the cache.
        Args:
            key: The key for the item.
            item: The item to be added.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache.
        Args:
            key: The key of the item to be retrieved.
        Returns:
            The item if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
