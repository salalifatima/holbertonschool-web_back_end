#!/usr/bin/env python3
"""
This module defines a function `sum_mixed_list` that calculates the sum of
elements in a list. The list can contain both integers and floats. The
function returns the sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all the integers and floats in the input list and returns the
    result as a float.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list containing integers and/or
    floats to be summed.

    Returns:
    float: The sum of all elements in the input list, cast to a float.
    """
    return float(sum(mxd_lst))
