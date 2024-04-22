#!/usr/bin/env python3
"""
Modul for task 6:
Write a type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats as arguments
and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of list of floats and integers in argument

    Args:
        List: list of float and integers: mxd_lst

    Returns:
        float: sum of number in list
    """
    sum: float = 0
    for number in mxd_lst:
        sum += number
    return sum
