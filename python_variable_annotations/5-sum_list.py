#!/usr/bin/env python3
"""
This module  typing Python defines a function `sum_list` that calculates\
the sum of all float values in a list.
It demonstrates the use of type annotations and the built-in `sum()` function.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums all the float values in the input list.

    Parameters:
    input_list (List[float]): A list of floats to be summed.

    Returns:
    float: The sum of all elements in the input list.
    """
    return sum(input_list)
