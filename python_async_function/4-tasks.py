#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that spawns multiple
task_wait_random tasks concurrently and returns their results
in the order they complete.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay and
    return the list of delays in ascending order of completion.
    """
    # Create tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results: List[float] = []

    # Collect results as tasks complete
    for completed in asyncio.as_completed(tasks):
        result = await completed
        results.append(result)

    return results
