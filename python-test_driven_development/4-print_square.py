#!/usr/bin/python3
"""Square printing module.

This module holds a single function, ``print_square``, which prints a
square made of the ``#`` character.
"""


def print_square(size):
    """Print a square of ``size`` by ``size`` using the ``#`` character.

    ``size`` must be an integer greater than or equal to zero, otherwise
    a TypeError or a ValueError is raised.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
