#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Test the creation of Rectangle instances."""

    def test_is_a_base(self):
        """A rectangle is an instance of Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_two_args(self):
        """Width and height alone give a default position."""
        rectangle = Rectangle(10, 2)
        self.assertEqual((rectangle.x, rectangle.y), (0, 0))

    def test_all_args(self):
        """Every argument is assigned to the right attribute."""
        rectangle = Rectangle(10, 2, 3, 4, 7)
        self.assertEqual(
            (rectangle.width, rectangle.height, rectangle.x,
             rectangle.y, rectangle.id), (10, 2, 3, 4, 7))

    def test_automatic_id(self):
        """Two rectangles without an id receive consecutive ids."""
        first = Rectangle(10, 2)
        second = Rectangle(10, 2)
        self.assertEqual(second.id, first.id + 1)

    def test_no_args(self):
        """Creating a rectangle without arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Creating a rectangle with only a width raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width_is_private(self):
        """The width attribute is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2).__width)


class TestRectangleValidation(unittest.TestCase):
    """Test the validation performed by the setters."""

    def test_width_string(self):
        """A string width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_width_float(self):
        """A float width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.5, 2)

    def test_width_none(self):
        """A None width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_width_zero(self):
        """A zero width raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        """A negative width raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_string(self):
        """A string height raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_height_zero(self):
        """A zero height raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        """A negative height raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_dictionary(self):
        """A dictionary x raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_x_negative(self):
        """A negative x raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_x_zero_is_valid(self):
        """A zero x is accepted."""
        self.assertEqual(Rectangle(10, 2, 0).x, 0)

    def test_y_string(self):
        """A string y raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")

    def test_y_negative(self):
        """A negative y raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_setter_validates(self):
        """Assigning through the setter validates the value too."""
        rectangle = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.width = -10


class TestRectangleArea(unittest.TestCase):
    """Test the area method."""

    def test_small(self):
        """The area of a small rectangle."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_square_shape(self):
        """The area of a rectangle with equal sides."""
        self.assertEqual(Rectangle(7, 7).area(), 49)

    def test_position_is_ignored(self):
        """The position does not change the area."""
        self.assertEqual(Rectangle(8, 7, 3, 4, 12).area(), 56)

    def test_one_by_one(self):
        """The smallest possible area."""
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_takes_no_argument(self):
        """Passing an argument to area raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Test the display method."""

    def capture(self, rectangle):
        """Return everything the rectangle prints."""
        output = io.StringIO()
        sys.stdout = output
        rectangle.display()
        sys.stdout = sys.__stdout__
        return output.getvalue()

    def test_simple(self):
        """A rectangle at the origin prints only hashes."""
        self.assertEqual(self.capture(Rectangle(2, 2)), "##\n##\n")

    def test_one_by_one(self):
        """The smallest rectangle prints a single hash."""
        self.assertEqual(self.capture(Rectangle(1, 1)), "#\n")

    def test_with_x(self):
        """A horizontal offset indents every row."""
        self.assertEqual(self.capture(Rectangle(2, 1, 3)), "   ##\n")

    def test_with_y(self):
        """A vertical offset prints empty lines first."""
        self.assertEqual(self.capture(Rectangle(2, 1, 0, 2)), "\n\n##\n")

    def test_with_x_and_y(self):
        """Both offsets are applied together."""
        self.assertEqual(
            self.capture(Rectangle(2, 3, 2, 2)),
            "\n\n  ##\n  ##\n  ##\n")


class TestRectangleStr(unittest.TestCase):
    """Test the __str__ method."""

    def test_full(self):
        """Every attribute appears in the representation."""
        rectangle = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rectangle), "[Rectangle] (12) 2/1 - 4/6")

    def test_default_position(self):
        """The default position appears as zeros."""
        rectangle = Rectangle(5, 5, 1, 0, 7)
        self.assertEqual(str(rectangle), "[Rectangle] (7) 1/0 - 5/5")

    def test_changes_with_update(self):
        """The representation follows the current values."""
        rectangle = Rectangle(4, 6, 2, 1, 12)
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")


class TestRectangleUpdate(unittest.TestCase):
    """Test the update method."""

    def test_args_id(self):
        """The first positional argument is the id."""
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89)
        self.assertEqual(rectangle.id, 89)

    def test_args_width(self):
        """The second positional argument is the width."""
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, 2)
        self.assertEqual(rectangle.width, 2)

    def test_args_all(self):
        """Five positional arguments set every attribute."""
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_args_extra_are_ignored(self):
        """Extra positional arguments are ignored."""
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_args_validates(self):
        """Positional arguments are validated."""
        rectangle = Rectangle(10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "invalid")

    def test_kwargs(self):
        """Keyword arguments set the named attributes."""
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(height=1)
        self.assertEqual(rectangle.height, 1)

    def test_kwargs_order_does_not_matter(self):
        """Keyword arguments can be given in any order."""
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/1 - 2/10")

    def test_kwargs_skipped_when_args(self):
        """Keyword arguments are ignored when positional ones exist."""
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89, width=5)
        self.assertEqual((rectangle.id, rectangle.width), (89, 10))

    def test_no_argument_changes_nothing(self):
        """Calling update without arguments leaves the object alone."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update()
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 10/10")


class TestRectangleToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def test_returns_a_dictionary(self):
        """The returned value is a dictionary."""
        self.assertEqual(type(Rectangle(10, 2, 1, 9).to_dictionary()), dict)

    def test_keys(self):
        """The dictionary holds the five expected keys."""
        result = Rectangle(10, 2, 1, 9, 1).to_dictionary()
        self.assertEqual(
            sorted(result.keys()), ["height", "id", "width", "x", "y"])

    def test_values(self):
        """The dictionary holds the current values."""
        result = Rectangle(10, 2, 1, 9, 1).to_dictionary()
        self.assertEqual(
            result, {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_used_by_update(self):
        """The dictionary can be fed back through update."""
        original = Rectangle(10, 2, 1, 9, 1)
        copy = Rectangle(1, 1)
        copy.update(**original.to_dictionary())
        self.assertEqual(str(copy), str(original))

    def test_takes_no_argument(self):
        """Passing an argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
