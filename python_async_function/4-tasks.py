#!/usr/bin/env python3
"""
Async routine called task_wait_n that takes in 2 int arguments (in this order):
n and max_delay. You will spawn wait_random n times with the specified
max_delay.
"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ Async routine """
    all_delays = []
    gather = await asyncio.gather(task_wait_random(max_delay))

    for _ in range(n):
        all_delays.append(gather[0])
    return all_delays
