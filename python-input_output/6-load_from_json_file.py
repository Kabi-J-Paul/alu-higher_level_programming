#!/usr/bin/python3
"""Module that builds a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from the JSON content of a file.

    Args:
        filename (str): the path of the JSON file to read.

    Returns:
        The Python object described by the file.
    """
    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
