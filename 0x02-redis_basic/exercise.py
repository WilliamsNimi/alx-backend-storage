#!/usr/bin/env python3
""" This is a Redis cache implementation """
from typing import Union, Callable
import redis
import uuid


class Cache:
    """ This is the Cache class"""
    def __init__(self) -> None:
        """ This is the constructor of class Cache """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ This is the store method
        @data: The data to be stored in redis cache
        Return: Returns a string
        """
        unique_id = str(uuid.uuid4())
        self._redis.set(unique_id, data)
        return unique_id

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """ This is the get method to convert a key
        @key: The key to be converted
        @fn: THe function to convert the key
        Return: returns nothing
        """
        byte_stream = self._redis.get(key)

        if fn is None or btye_stream is None:
            return byte_stream

        return fn(byte_stream)

    def get_str(self, value: bytes) -> str:
        """
        this is the get_str function for redis parameterization
        @value: Bytes value to convert
        @Returns: returns a string value
        """
        return str(value)

    def get_int(self, value: bytes) -> int:
        """ This is the get in function
        @value: The value to be converted
        Returns: returns an integer value
        """
        return int(value)
