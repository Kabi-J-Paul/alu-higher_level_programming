#!/usr/bin/python3
"""Matrix division module.

This module holds a single function, ``matrix_divided``, which divides
every element of a matrix by a number and returns a new matrix, leaving
the original untouched.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements of ``matrix`` divided by ``div``.

    Every result is rounded to 2 decimal places. The matrix must be a
    list of lists of integers or floats with rows of equal size.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(message)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(message)
        for element in row:
            if not isinstance(element, (int, float)) or isinstance(
                    element, bool):
                raise TypeError(message)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
