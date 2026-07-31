#!/usr/bin/python3
"""Module that checks whether an object comes from a strict subclass."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class.

    Args:
        obj: the object to check.
        a_class: the class that should be an ancestor of the type of obj.

    Returns:
        True if the type of obj is a strict subclass of a_class,
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
