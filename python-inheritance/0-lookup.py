#!/usr/bin/python3
"""Module that provides a function to inspect an object's interface."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: the object to inspect.

    Returns:
        A list of the names of the attributes and methods of obj.
    """
    return dir(obj)
