#!/usr/bin/env python 3
"""
h
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n:int, max_delay: int) -> float:
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    
    return total_time / n
