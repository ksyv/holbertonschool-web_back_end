#!/usr/bin/env python3
"""
Modul for task 10:
Augment the following code
with the correct duck-typed annotations:
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely returns first element of sequence, or None if sequence is empty.

    Args:
    lst (Sequence[Any]): Sequence of elements from wich to get first element.

    Returns:
    Optional[Any]: First element of sequence, or None if sequence is empty.
    """
    return lst[0] if lst else None
