#!/usr/bin/env python3
"""
This module defines a function `make_multiplier` that returns a function
which multiplies its input by a specified multiplier. The multiplier is
provided when calling `make_multiplier`.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The value to multiply by.

    Returns:
    Callable[[float], float]: A function that takes a float and returns a
    float, which is the result of multiplying the input by `multiplier`.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier

    return multiplier_function
