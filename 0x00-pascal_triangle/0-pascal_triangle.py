#!/usr/bin/python3
"""Defines pascal_triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s
    triangle of n.

    Arguments:
        n (int): Height of the triangle.
    """
    triangle = []

    for i in range(0, n):
        if i == 0:
            triangle.append([1])
        else:
            new_row = []
            prev_row = triangle[-1]
            new_row.append(1)

            j = 0
            k = 1
            while k < len(prev_row):
                new_row.append(prev_row[j] + prev_row[k])
                j += 1
                k += 1
            new_row.append(1)
            triangle.append(new_row)
    return triangle
