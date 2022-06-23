#!/usr/bin/python3
"""Solution for the Lockboxes problem."""


def canUnlockAll(boxes):
    """Problem: You have n number of locked boxes in front of you. Each box is
    numbered sequentially from 0 to n - 1 and each box may contain keys to the
    other boxes.

    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - There can be keys that do not have boxes
    - The first box boxes[0] is unlocked
    Returns True if all boxes can be opened, else return False
    """
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
