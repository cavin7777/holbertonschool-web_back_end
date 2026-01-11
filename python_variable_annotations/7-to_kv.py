#!/usr/bin/env python3
"""
This module provides a function that returns a key-value tuple
where the value is squared.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string key and the square of a number.
    """
    return (k, float(v * v))
