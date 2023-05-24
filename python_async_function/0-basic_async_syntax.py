#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an integer argument (max_delay, with a
default value of 10) named wait_random that waits for a random delay between
0 and max_delay (included and float value) seconds and eventually returns it.
"""
import random
import asyncio
import timeit


async def wait_random(max_delay: int = 10) -> float:
    random_number = random.randint(0, max_delay)
    time_start = timeit.default_timer()
    seconds = await asyncio.sleep(random_number)
    time_end = timeit.default_timer()

    return (time_start - time_end - 1) * - 1
