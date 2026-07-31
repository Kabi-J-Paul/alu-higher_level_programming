#!/usr/bin/python3
"""Module that saves a Python object to a file as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj: the object to serialize and save.
        filename (str): the path of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
