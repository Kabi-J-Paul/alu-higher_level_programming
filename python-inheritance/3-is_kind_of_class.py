#!/usr/bin/python3
"""Module that checks whether an object is of a class or a subclass of it."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or of a subclass of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare obj against.

    Returns:
        True if obj is an instance of a_class or of one of its
        subclasses, otherwise False.
    """
    return isinstance(obj, a_class)
