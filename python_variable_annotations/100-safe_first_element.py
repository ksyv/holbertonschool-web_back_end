#!/usr/bin/env python3
"""
Modul for task 10:
Augment the following code
with the correct duck-typed annotations:
# The types of the elements of the input are not known
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Args:
            lst: Any data type

        Return:
            None or first element
    """
    if lst:
        return lst[0]
    else:
        return None
