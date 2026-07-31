#!/usr/bin/python3
"""Module that describes an instance with a serializable dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an instance for JSON.

    Only the instance attributes are returned, and they are assumed to
    all be serializable: list, dictionary, string, integer and boolean.

    Args:
        obj: an instance of a class.

    Returns:
        A dictionary of the attributes of obj.
    """
    return obj.__dict__.copy()
