#!/usr/bin/python3
"""Defines a function named validUTF8."""
import chardet


def validUTF8(data):
    """Returns True if a given data set represents a valid UTF-8 encoding.
    Otherwise, return False.
    """
    for integer in data:
        result = chardet.detect(chr(integer).encode("utf-8"))
        # print(result)
        if result['confidence'] < 80:
            return True
        encoding = result["encoding"]
        if encoding != "ascii":
            return False
    return True
 