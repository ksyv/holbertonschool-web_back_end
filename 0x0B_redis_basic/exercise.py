#!/usr/bin/env python3
"""
Modul for writing string to Redis
"""
import redis
import uuid
from typing import Union, Callable
import functools


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method is called."""
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper around the method to increment the counter and call the original method."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method:Callable) -> Callable:
    """decorator to store the history of inputs ans outputs"""
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"
    
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper around the method to store inputs and outputs"""
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)
        return output
    return wrapper

class Cache:
    """Storing data in redis"""
    def __init__(self):
        """init redis and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
