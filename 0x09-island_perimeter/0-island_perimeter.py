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
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
