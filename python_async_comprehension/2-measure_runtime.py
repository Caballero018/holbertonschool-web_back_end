#!/usr/bin/env python3
"""
Coroutine that will execute async_comprehension four times in
parallel using asyncio.gather.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Coroutine that will execute async_comprehension """
    start = time.time()
    await asyncio.gather(async_comprehension())
    total_time = time.time() - start

    return total_time
