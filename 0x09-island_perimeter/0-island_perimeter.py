#!/usr/bin/python3
"""Defines the function island_perimeter."""


def island_perimeter(grid):
    """Computes the perimeter of an island described in grid.
    Returns the perimeter of the island.
    """
    perimeter = 0

    col = len(grid)
    row = len(grid[0])

    for i in range(col):
        for j in range(row):
            if grid[i][j] == 1:
                try:
                    nth = grid[i - 1][j]
                    sth = grid[i + 1][j]
                    est = grid[i][j + 1]
                    wst = grid[i][j - 1]
                except IndexError:
                    pass

                for direction in [nth, sth, est, wst]:
                    if direction == 0:
                        perimeter += 1

    return perimeter
