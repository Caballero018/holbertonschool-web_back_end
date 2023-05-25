#!/usr/bin/env python 3
"""
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n:int, max_delay: int) -> float:
    start = time.perf_counter()
    await asyncio.gather(wait_n(n, max_delay))
    total_time  = time.perf_counter() - start
    return total_time  / n 
