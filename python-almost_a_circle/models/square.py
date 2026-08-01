#!/usr/bin/python3
"""Square module.

This module defines the ``Square`` class, which inherits from
``Rectangle``. A square is a rectangle whose width and height are
always equal, so it reuses every attribute of its parent.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square defined by its size and its position.

    The size is stored as the width and the height of the underlying
    rectangle, so all the validation of ``Rectangle`` still applies.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square with its size, position and id."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and the height of the square to the same value."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the informal string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign arguments to attributes, by position or by keyword."""
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
