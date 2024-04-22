#!/usr/bin/env python3
"""
Modul for task 7:
Write a type-annotated function make_multiplier that takes
a float multiplier as arguments
and returns function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function that multiplies a float by multiplier

    Args:
        multiplier(float): the multiplier

    Returns:
        function that multiplies a float by multiplier
    """
    def multiplyFunction(f: float) -> float:
        """get second arg and make the multiply"""
        return float(f * multiplier)
    return multiplyFunction
