#!/usr/bin/python3
"""Name printing module.

This module holds a single function, ``say_my_name``, which prints a
full name in a fixed sentence format.
"""


def say_my_name(first_name, last_name=""):
    """Print ``My name is <first name> <last name>``.

    Both arguments must be strings, otherwise a TypeError is raised.
    The last name is optional and defaults to an empty string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
