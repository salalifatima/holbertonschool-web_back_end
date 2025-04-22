#!/usr/bin/env python3
"""
Module defines `to_kv`, a function that returns a tuple containing a string
and the square of a number (int or float) as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string `k` and the square of `v` as a float.

    Parameters:
    k (str): The key.
    v (Union[int, float]): The value to square.

    Returns:
    Tuple[str, float]: A tuple with `k` and the square of `v`.
    """
    return (k, float(v ** 2))
