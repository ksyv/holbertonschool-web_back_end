#!/usr/bin/env python3
"""
Modul for task 1:
Import wait_random from the previous python file
that you’ve written and write an async routine called wait_n
that takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without
using sort() because of concurrency.
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
        Args:
            n(int): number of applicated max_delay
            max_delay(int): max delay of wait

        Return:
            list of all the delay sorted
    """
    list = []
    for i in range(n):
        list.append(wait_random(max_delay))
    return [await i for i in asyncio.as_completed(list)]
