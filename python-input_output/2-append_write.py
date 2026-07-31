#!/usr/bin/python3
"""Module that provides a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file.

    The file is created if it does not exist yet.

    Args:
        filename (str): the path of the file to append to.
        text (str): the string to add at the end of the file.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
