#!/usr/bin/env python3
"""
This module measures the total runtime of wait_n coroutines
and returns the average runtime per coroutine.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total runtime of wait_n(n, max_delay) coroutines
    and return the average runtime per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
