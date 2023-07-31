#!/usr/bin/env python3
"""
Module that have a function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay), and
returns total_time / n.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function with integers n and max_delay as arguments that measures the
    total    execution time for wait_n(n, max_delay), and returns total_time
    / n.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start

    return total_time / n
