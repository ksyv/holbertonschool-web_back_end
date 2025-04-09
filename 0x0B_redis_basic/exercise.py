#!/usr/bin/env python3
"""
Modul for writing string to Redis
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """Storing data in redis"""
    def __init__(self):
        """init redis and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the input data in Redis using the random key and return the key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
    
    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        take a key string argument and an optional Callable argument 
        named fn. This callable will be used to convert the data back to the 
        desired format.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Union[str, None]:
        """Get a str by Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """Get an int by Redis."""
        return self.get(key, fn=int)
