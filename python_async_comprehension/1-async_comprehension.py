#!/usr/bin/env python3
"""
Modul for task 1:
Import async_generator from the previous task and then write
a coroutine called async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        List[float]: _description_
    """
    return [i async for i in async_generator()]
