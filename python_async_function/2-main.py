#!/usr/bin/env python3
import asyncio
measure_time = __import__('2-measure_runtime').measure_time
wait_n = __import__('1-concurrent_coroutines').wait_n
wait_random = __import__('0-basic_async_syntax').wait_random

n = 5
max_delay = 9

print(asyncio.run(wait_n(n, 5)))
print(measure_time(n, max_delay))
