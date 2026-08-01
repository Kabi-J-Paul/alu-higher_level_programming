#!/usr/bin/python3
"""Text indentation module.

This module holds a single function, ``text_indentation``, which prints
a text with two new lines after each of the characters ``.``, ``?``
and ``:``.
"""


def text_indentation(text):
    """Print ``text`` with two new lines after each ``.``, ``?`` or ``:``.

    Spaces at the beginning and at the end of each printed line are
    removed. The argument must be a string, otherwise a TypeError is
    raised.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    index = 0
    while index < len(text):
        print(text[index], end="")
        if text[index] in ".?:":
            print("\n")
            index += 1
            while index < len(text) and text[index] == " ":
                index += 1
            continue
        index += 1
