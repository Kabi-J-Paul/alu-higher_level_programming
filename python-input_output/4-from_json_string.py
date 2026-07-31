#!/usr/bin/python3
"""Module that deserializes a JSON string into a Python object."""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): the JSON string to deserialize.

    Returns:
        The Python object built from my_str.
    """
    return json.loads(my_str)
