#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Test the creation of Base instances and their ids."""

    def test_id_is_given(self):
        """A given id is used as is."""
        self.assertEqual(Base(89).id, 89)

    def test_id_is_none(self):
        """An automatic id is assigned when none is given."""
        base_one = Base()
        base_two = Base()
        self.assertEqual(base_two.id, base_one.id + 1)

    def test_negative_id(self):
        """A negative id is accepted without validation."""
        self.assertEqual(Base(-5).id, -5)

    def test_zero_id(self):
        """A zero id is accepted without validation."""
        self.assertEqual(Base(0).id, 0)

    def test_string_id(self):
        """A string id is accepted without validation."""
        self.assertEqual(Base("hello").id, "hello")

    def test_nb_objects_is_private(self):
        """The instance counter is not publicly accessible."""
        with self.assertRaises(AttributeError):
            print(Base(1).__nb_objects)

    def test_two_args(self):
        """Passing two arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Test the to_json_string static method."""

    def test_none(self):
        """None returns an empty list representation."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list returns an empty list representation."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_returns_a_string(self):
        """The returned value is a string."""
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(type(result), str)

    def test_one_dictionary(self):
        """A single dictionary is serialized correctly."""
        result = Base.to_json_string([{"id": 9, "width": 5}])
        self.assertEqual(json.loads(result), [{"id": 9, "width": 5}])

    def test_two_dictionaries(self):
        """Two dictionaries produce a list of length two."""
        result = Base.to_json_string([{"id": 1}, {"id": 2}])
        self.assertEqual(len(json.loads(result)), 2)

    def test_no_argument(self):
        """Calling without an argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestBaseFromJsonString(unittest.TestCase):
    """Test the from_json_string static method."""

    def test_none(self):
        """None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_returns_a_list(self):
        """The returned value is a list."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(type(result), list)

    def test_one_dictionary(self):
        """A single dictionary is deserialized correctly."""
        result = Base.from_json_string('[{"id": 9, "width": 5}]')
        self.assertEqual(result, [{"id": 9, "width": 5}])

    def test_two_dictionaries(self):
        """Two dictionaries produce a list of length two."""
        result = Base.from_json_string('[{"id": 1}, {"id": 2}]')
        self.assertEqual(len(result), 2)

    def test_no_argument(self):
        """Calling without an argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBaseCreate(unittest.TestCase):
    """Test the create class method."""

    def test_rectangle(self):
        """A rectangle is rebuilt from its dictionary."""
        rectangle = Rectangle(3, 5, 1, 2, 7)
        copy = Rectangle.create(**rectangle.to_dictionary())
        self.assertEqual(str(copy), str(rectangle))

    def test_rectangle_is_a_new_object(self):
        """The created rectangle is not the original one."""
        rectangle = Rectangle(3, 5, 1, 2, 7)
        copy = Rectangle.create(**rectangle.to_dictionary())
        self.assertIsNot(copy, rectangle)

    def test_square(self):
        """A square is rebuilt from its dictionary."""
        square = Square(4, 1, 2, 7)
        copy = Square.create(**square.to_dictionary())
        self.assertEqual(str(copy), str(square))

    def test_square_is_a_new_object(self):
        """The created square is not the original one."""
        square = Square(4, 1, 2, 7)
        copy = Square.create(**square.to_dictionary())
        self.assertIsNot(copy, square)


class TestBaseSaveToFile(unittest.TestCase):
    """Test the save_to_file class method."""

    def tearDown(self):
        """Remove the files created by the tests."""
        for name in ("Rectangle.json", "Square.json", "Base.json"):
            try:
                os.remove(name)
            except FileNotFoundError:
                pass

    def test_none(self):
        """Saving None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_empty_list(self):
        """Saving an empty list writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_one_rectangle(self):
        """Saving one rectangle writes one dictionary."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(len(json.loads(a_file.read())), 1)

    def test_two_squares(self):
        """Saving two squares writes two dictionaries."""
        Square.save_to_file([Square(5), Square(7, 9, 1)])
        with open("Square.json", "r") as a_file:
            self.assertEqual(len(json.loads(a_file.read())), 2)

    def test_overwrites(self):
        """Saving twice overwrites the previous content."""
        Rectangle.save_to_file([Rectangle(10, 7)])
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")


class TestBaseLoadFromFile(unittest.TestCase):
    """Test the load_from_file class method."""

    def tearDown(self):
        """Remove the files created by the tests."""
        for name in ("Rectangle.json", "Square.json"):
            try:
                os.remove(name)
            except FileNotFoundError:
                pass

    def test_no_file(self):
        """Loading a missing file returns an empty list."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_returns_a_list(self):
        """The returned value is a list."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        self.assertEqual(type(Rectangle.load_from_file()), list)

    def test_rectangle_instances(self):
        """The loaded objects are rectangles."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        loaded = Rectangle.load_from_file()
        self.assertEqual(type(loaded[0]), Rectangle)

    def test_square_instances(self):
        """The loaded objects are squares."""
        Square.save_to_file([Square(5, 1, 2, 3)])
        loaded = Square.load_from_file()
        self.assertEqual(type(loaded[0]), Square)

    def test_same_values(self):
        """The loaded rectangle holds the saved values."""
        original = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([original])
        loaded = Rectangle.load_from_file()
        self.assertEqual(str(loaded[0]), str(original))


if __name__ == "__main__":
    unittest.main()
