#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random
amount of time before returning the delay.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return it.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
