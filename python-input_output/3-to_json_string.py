#!/usr/bin/python3
"""Module that serializes a Python object into a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj: the object to serialize.

    Returns:
        The JSON string describing my_obj.
    """
    return json.dumps(my_obj)
