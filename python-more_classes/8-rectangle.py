#!/usr/bin/python3
"""Defines a Rectangle class that can compare rectangles by area."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances alive.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the rectangle drawn with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        rows = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        """Return a string representation able to recreate the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If either argument is not a Rectangle.

        Returns:
            rect_1 if both rectangles have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
