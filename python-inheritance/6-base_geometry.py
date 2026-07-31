#!/usr/bin/python3
"""Module that defines a base class for geometry shapes with an area."""


class BaseGeometry:
    """Represent the base class of every geometry shape."""

    def area(self):
        """Raise an exception because the area is not implemented here."""
        raise Exception("area() is not implemented")
