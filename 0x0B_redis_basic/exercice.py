#!/usr/bin/env python3
"""
Modul for writing string to Redis
"""
import redis
import uuid
from typing import Union


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
        self.redis.set(random_key, data)
        return random_key
