#!/usr/bin/python3
"""Addition module.

This module holds a single function, ``add_integer``, which adds two
numbers together. Both numbers are casted to integers before the
addition is performed, so floats are truncated toward zero.
"""


def add_integer(a, b=98):
    """Return the addition of ``a`` and ``b`` as an integer.

    ``a`` and ``b`` must be integers or floats, otherwise a TypeError
    is raised. Floats are casted to integers before being added.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
