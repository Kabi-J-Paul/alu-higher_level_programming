#!/usr/bin/python3
"""Unittests for the ``max_integer`` function."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases covering the behaviour of ``max_integer``."""

    def test_ordered_list(self):
        """The maximum is the last element of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The maximum is found anywhere in the list."""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_max_at_beginning(self):
        """The maximum is the first element of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Calling without an argument uses the empty default list."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """A list of one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Negative numbers are compared correctly."""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_duplicated_max(self):
        """A repeated maximum is returned once."""
        self.assertEqual(max_integer([3, 9, 9, 2]), 9)

    def test_floats(self):
        """Floats are compared like any other number."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_numbers(self):
        """Integers and floats can be mixed in the same list."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_strings(self):
        """A list of strings is compared alphabetically."""
        self.assertEqual(max_integer(["apple", "pear", "banana"]), "pear")

    def test_one_string(self):
        """A single string is compared character by character."""
        self.assertEqual(max_integer("hello"), "o")

    def test_mixed_types(self):
        """Comparing a string with an integer raises a TypeError."""
        self.assertRaises(TypeError, max_integer, [1, "two", 3])

    def test_none_argument(self):
        """Passing None raises a TypeError."""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
