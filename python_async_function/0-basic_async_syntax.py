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
    """ Asynchronous coroutine """
    # Random number
    random_number = random.randint(0, max_delay)

    # Start time
    start_time = timeit.default_timer()

    # Wait time
    await asyncio.sleep(random_number)

    # End time
    end_time = timeit.default_timer()

    return (start_time - end_time - 1) * -1
