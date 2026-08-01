#!/usr/bin/python3
"""Unittests for the Square class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Test the creation of Square instances."""

    def test_is_a_rectangle(self):
        """A square is an instance of Rectangle."""
        self.assertIsInstance(Square(5), Rectangle)

    def test_is_a_base(self):
        """A square is an instance of Base."""
        self.assertIsInstance(Square(5), Base)

    def test_size_sets_both_sides(self):
        """The size is used as the width and the height."""
        square = Square(5)
        self.assertEqual((square.width, square.height), (5, 5))

    def test_default_position(self):
        """A square without a position sits at the origin."""
        square = Square(5)
        self.assertEqual((square.x, square.y), (0, 0))

    def test_all_args(self):
        """Every argument is assigned to the right attribute."""
        square = Square(5, 1, 2, 7)
        self.assertEqual(
            (square.size, square.x, square.y, square.id), (5, 1, 2, 7))

    def test_automatic_id(self):
        """Two squares without an id receive consecutive ids."""
        first = Square(5)
        second = Square(5)
        self.assertEqual(second.id, first.id + 1)

    def test_no_args(self):
        """Creating a square without arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        """Passing five arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquareValidation(unittest.TestCase):
    """Test that the square inherits the validation of the rectangle."""

    def test_size_string(self):
        """A string size raises a TypeError mentioning the width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_float(self):
        """A float size raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_size_none(self):
        """A None size raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_size_zero(self):
        """A zero size raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_negative(self):
        """A negative size raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_x_negative(self):
        """A negative x raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)

    def test_y_string(self):
        """A string y raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, "2")

    def test_setter_validates(self):
        """The size setter validates the value."""
        square = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.size = "9"


class TestSquareSize(unittest.TestCase):
    """Test the size getter and setter."""

    def test_getter(self):
        """The getter returns the current size."""
        self.assertEqual(Square(5).size, 5)

    def test_setter_changes_both_sides(self):
        """The setter changes the width and the height together."""
        square = Square(5)
        square.size = 10
        self.assertEqual((square.width, square.height), (10, 10))

    def test_setter_changes_representation(self):
        """The representation follows the new size."""
        square = Square(5, 0, 0, 1)
        square.size = 10
        self.assertEqual(str(square), "[Square] (1) 0/0 - 10")

    def test_width_setter_still_works(self):
        """The inherited width setter is still available."""
        square = Square(5)
        square.width = 7
        self.assertEqual(square.size, 7)


class TestSquareArea(unittest.TestCase):
    """Test the inherited area method."""

    def test_small(self):
        """The area of a small square."""
        self.assertEqual(Square(5).area(), 25)

    def test_one_by_one(self):
        """The smallest possible area."""
        self.assertEqual(Square(1).area(), 1)

    def test_position_is_ignored(self):
        """The position does not change the area."""
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_follows_size(self):
        """The area follows a change of size."""
        square = Square(2)
        square.size = 4
        self.assertEqual(square.area(), 16)


class TestSquareDisplay(unittest.TestCase):
    """Test the inherited display method."""

    def capture(self, square):
        """Return everything the square prints."""
        output = io.StringIO()
        sys.stdout = output
        square.display()
        sys.stdout = sys.__stdout__
        return output.getvalue()

    def test_simple(self):
        """A square at the origin prints only hashes."""
        self.assertEqual(self.capture(Square(2)), "##\n##\n")

    def test_one_by_one(self):
        """The smallest square prints a single hash."""
        self.assertEqual(self.capture(Square(1)), "#\n")

    def test_with_x(self):
        """A horizontal offset indents every row."""
        self.assertEqual(self.capture(Square(2, 2)), "  ##\n  ##\n")

    def test_with_x_and_y(self):
        """Both offsets are applied together."""
        self.assertEqual(
            self.capture(Square(2, 1, 2)), "\n\n ##\n ##\n")


class TestSquareStr(unittest.TestCase):
    """Test the __str__ method."""

    def test_full(self):
        """Every attribute appears in the representation."""
        self.assertEqual(str(Square(3, 1, 3, 7)), "[Square] (7) 1/3 - 3")

    def test_default_position(self):
        """The default position appears as zeros."""
        self.assertEqual(str(Square(5, 0, 0, 1)), "[Square] (1) 0/0 - 5")

    def test_one_side_only(self):
        """Only one side is shown, unlike a rectangle."""
        self.assertNotIn("/5 - 5", str(Square(5, 0, 0, 1)))


class TestSquareUpdate(unittest.TestCase):
    """Test the update method."""

    def test_args_id(self):
        """The first positional argument is the id."""
        square = Square(5)
        square.update(10)
        self.assertEqual(square.id, 10)

    def test_args_size(self):
        """The second positional argument is the size."""
        square = Square(5)
        square.update(1, 2)
        self.assertEqual(square.size, 2)

    def test_args_all(self):
        """Four positional arguments set every attribute."""
        square = Square(5)
        square.update(1, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_args_extra_are_ignored(self):
        """Extra positional arguments are ignored."""
        square = Square(5)
        square.update(1, 2, 3, 4, 5)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_args_validates(self):
        """Positional arguments are validated."""
        square = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(1, "invalid")

    def test_kwargs(self):
        """Keyword arguments set the named attributes."""
        square = Square(5, 0, 0, 1)
        square.update(x=12)
        self.assertEqual(str(square), "[Square] (1) 12/0 - 5")

    def test_kwargs_order_does_not_matter(self):
        """Keyword arguments can be given in any order."""
        square = Square(5, 0, 0, 1)
        square.update(size=7, id=89, y=1)
        self.assertEqual(str(square), "[Square] (89) 0/1 - 7")

    def test_kwargs_skipped_when_args(self):
        """Keyword arguments are ignored when positional ones exist."""
        square = Square(5)
        square.update(89, size=1)
        self.assertEqual((square.id, square.size), (89, 5))

    def test_no_argument_changes_nothing(self):
        """Calling update without arguments leaves the object alone."""
        square = Square(5, 0, 0, 1)
        square.update()
        self.assertEqual(str(square), "[Square] (1) 0/0 - 5")


class TestSquareToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def test_returns_a_dictionary(self):
        """The returned value is a dictionary."""
        self.assertEqual(type(Square(10, 2, 1).to_dictionary()), dict)

    def test_keys(self):
        """The dictionary holds the four expected keys."""
        result = Square(10, 2, 1, 7).to_dictionary()
        self.assertEqual(sorted(result.keys()), ["id", "size", "x", "y"])

    def test_no_width_or_height(self):
        """The dictionary uses size instead of width and height."""
        result = Square(10, 2, 1, 7).to_dictionary()
        self.assertNotIn("width", result)

    def test_values(self):
        """The dictionary holds the current values."""
        result = Square(10, 2, 1, 7).to_dictionary()
        self.assertEqual(result, {"id": 7, "size": 10, "x": 2, "y": 1})

    def test_used_by_update(self):
        """The dictionary can be fed back through update."""
        original = Square(10, 2, 1, 7)
        copy = Square(1)
        copy.update(**original.to_dictionary())
        self.assertEqual(str(copy), str(original))


if __name__ == "__main__":
    unittest.main()
