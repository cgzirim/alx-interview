#!/usr/bin/python3
"""Defines a function called minOperations."""


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations needed to result in
    exactly n H characters in a string."""
    text = "H"
    cmd_count = 0
    copied_text = ""

    # Copy all text
    copied_text = text

    for i in range(n):
        if len(text) == n:
            return cmd_count

        # Paste all copied text
        text = text + copied_text
        cmd_count += 1

        if len(text) != 1 and n % len(text) == 0:
            # Copy all text
            copied_text = text
            cmd_count += 1

    return cmd_count
