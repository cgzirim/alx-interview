#!/usr/bin/python3
"""Defines a function named validUTF8."""
from typing import List


def validUTF8(data: List) -> bool:
    """Returns True if a given data set represents a valid UTF-8 encoding.
    Otherwise, return False.
    """
    for integer in data:
        if integer > 255 or elem < 0:
            return False
    return True
