#!/usr/bin/env python3
"""
This module with tyoing Python
contains concat() function with type annotation.
"""


def concat(str1: str, str2: str) -> str:
    """
    This function concatenates two strings.
        Args:
            str1: The first string (str).
            str2: The second string (str).
        Return:
            The concatenation of the `str1` and `str2`  (str).
    """
    return str1 + str2
