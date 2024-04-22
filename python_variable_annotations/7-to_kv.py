#!/usr/bin/env python3
"""
Modul for task 7:
Write a type-annotated function to_kv that takes
a string k and an int OR float v as arguments
and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v
and should be annotated as a float. 
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple with: string k and square of v

    Args:
        k (str): string argument
        v (int or float): number argument 

    Returns:
        Tuple: string k, square of v
    """
    mixed_tuple: Tuple[str, float]
    mixed_tuple = (k, v**2)
    return mixed_tuple
