#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix by 90 degrees clockwise."""
    org_matrix = matrix
    rotated_matrix = []

    i = 0
    while i < len(org_matrix):
        new_row = []

        for row in org_matrix:
            new_row.append(row[i])
        new_row.reverse()
        rotated_matrix.append(new_row)

        i += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = rotated_matrix[i][j]
