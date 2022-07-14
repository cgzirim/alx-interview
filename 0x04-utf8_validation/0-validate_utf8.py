#!/usr/bin/python3
"""Defines a function named validUTF8."""
import chardet
from typing import List


def validUTF8(data: List) -> bool:
    """Returns True if a given data set represents a valid UTF-8 encoding.
    Otherwise, return False.
    """
    for integer in data:
        result = chardet.detect(chr(integer).encode('utf-8'))
        encoding = result['encoding']
        if encoding != 'ascii':
            return False
    return True
