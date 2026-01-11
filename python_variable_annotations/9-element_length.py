#!/usr/bin/env python3
"""
This module provides a function that returns each element of an iterable
together with its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element of the iterable
    and its length.
    """
    return [(i, len(i)) for i in lst]
