#!/usr/bin/env python3
"""
This module provides a function that creates and returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a fixed multiplier.
    """

    def multiply(value: float) -> float:
        """
        Multiplies a value by the outer multiplier.
        """
        return value * multiplier

    return multiply
