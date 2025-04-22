#!/usr/bin/env python3
"""
This module defines a function `element_length` that takes an iterable of
sequences (such as strings or lists) and returns a list of tuples, where
each tuple contains the sequence and its length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences (e.g., strings, lists) and returns a list
    of tuples, each containing a sequence and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences (e.g., list of strings).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
    a sequence and its length (integer).
    """
    return [(i, len(i)) for i in lst]
