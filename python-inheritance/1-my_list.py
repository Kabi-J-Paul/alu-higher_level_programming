#!/usr/bin/python3
"""Module that defines a list subclass able to print itself sorted."""


class MyList(list):
    """A list that can print its elements in ascending order."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
