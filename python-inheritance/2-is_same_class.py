#!/usr/bin/python3
"""Module that checks whether an object is exactly of a given class."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare the type of obj against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
