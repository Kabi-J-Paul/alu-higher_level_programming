#!/usr/bin/python3
"""Module that provides a function to write a string into a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file, overwriting any old content.

    The file is created if it does not exist yet.

    Args:
        filename (str): the path of the file to write to.
        text (str): the string to write in the file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
