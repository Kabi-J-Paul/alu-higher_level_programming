#!/usr/bin/python3
"""Module that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of n as a list of lists of integers.

    Each row starts and ends with 1, and every other value is the sum of
    the two values above it in the previous row.

    Args:
        n (int): the number of rows of the triangle.

    Returns:
        A list of n lists of integers, or an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for row_number in range(1, n):
        previous = triangle[-1]
        row = [1]
        for i in range(len(previous) - 1):
            row.append(previous[i] + previous[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
