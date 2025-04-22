#!/usr/bin/env python3

"""
This module provides a custom implementation of the floor function,
which returns the greatest integer less than or equal to the given number.
"""


def floor(n: float) -> int:
    """
    Returns the greatest integer less than or equal to `n`.

    If `n` is negative, it rounds down to the next lower integer.

    Parameters:
    n (float): The number to floor.

    Returns:
    int: The floored integer.
    """
    if n < 0:
        return int(n) + 1
    return int(n)
