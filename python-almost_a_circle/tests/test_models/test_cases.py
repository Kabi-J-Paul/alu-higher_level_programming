#!/usr/bin/python3
"""Unittests covering the exact argument combinations checked."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareCases(unittest.TestCase):
    """Cover every documented Square argument combination."""

    def test_square_size_1(self):
        """A bad size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square("2")

    def test_square_size_2(self):
        """A bad size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(2.5)

    def test_square_size_3(self):
        """A bad size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(None)

    def test_square_size_4(self):
        """A bad size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square({})

    def test_square_size_5(self):
        """A bad size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square([])

    def test_square_size_6(self):
        """A bad size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square((1,))

    def test_square_size_7(self):
        """A bad size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(float("inf"))

    def test_square_size_8(self):
        """A bad size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(float("nan"))

    def test_square_x_9(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_x_10(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2.5)

    def test_square_x_11(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, None)

    def test_square_x_12(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, {})

    def test_square_x_13(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, [])

    def test_square_x_14(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, (1,))

    def test_square_x_15(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, float("inf"))

    def test_square_x_16(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, float("nan"))

    def test_square_y_17(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, "2")

    def test_square_y_18(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 2.5)

    def test_square_y_19(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, None)

    def test_square_y_20(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, {})

    def test_square_y_21(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, [])

    def test_square_y_22(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, (1,))

    def test_square_y_23(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, float("inf"))

    def test_square_y_24(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, float("nan"))

    def test_square_value_25(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_value_26(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_value_27(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Square(-3)

    def test_square_value_28(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_value_29(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_value_30(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -2, -3)

    def test_square_value_31(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Square(0, 0)

    def test_square_value_32(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Square(-1, -1, -1)

    def test_square_valid_33(self):
        """A valid square is created."""
        self.assertIsInstance(Square(1), Square)

    def test_square_valid_34(self):
        """A valid square is created."""
        self.assertIsInstance(Square(1, 2), Square)

    def test_square_valid_35(self):
        """A valid square is created."""
        self.assertIsInstance(Square(1, 2, 3), Square)

    def test_square_valid_36(self):
        """A valid square is created."""
        self.assertIsInstance(Square(1, 2, 3, 4), Square)

    def test_square_valid_37(self):
        """A valid square is created."""
        self.assertIsInstance(Square(5), Square)

    def test_square_valid_38(self):
        """A valid square is created."""
        self.assertIsInstance(Square(10, 2, 1), Square)


class TestRectangleCases(unittest.TestCase):
    """Cover every documented Rectangle argument combination."""

    def test_rect_width_39(self):
        """A bad width raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("2", 2)

    def test_rect_width_40(self):
        """A bad width raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(2.5, 2)

    def test_rect_width_41(self):
        """A bad width raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(None, 2)

    def test_rect_width_42(self):
        """A bad width raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle({}, 2)

    def test_rect_width_43(self):
        """A bad width raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle([], 2)

    def test_rect_width_44(self):
        """A bad width raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle((1,), 2)

    def test_rect_width_45(self):
        """A bad width raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(float("inf"), 2)

    def test_rect_width_46(self):
        """A bad width raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(float("nan"), 2)

    def test_rect_height_47(self):
        """A bad height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rect_height_48(self):
        """A bad height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2.5)

    def test_rect_height_49(self):
        """A bad height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, None)

    def test_rect_height_50(self):
        """A bad height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, {})

    def test_rect_height_51(self):
        """A bad height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, [])

    def test_rect_height_52(self):
        """A bad height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, (1,))

    def test_rect_height_53(self):
        """A bad height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, float("inf"))

    def test_rect_height_54(self):
        """A bad height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, float("nan"))

    def test_rect_x_55(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "2")

    def test_rect_x_56(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 2.5)

    def test_rect_x_57(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, None)

    def test_rect_x_58(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {})

    def test_rect_x_59(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [])

    def test_rect_x_60(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, (1,))

    def test_rect_x_61(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, float("inf"))

    def test_rect_x_62(self):
        """A bad x raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, float("nan"))

    def test_rect_y_63(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "2")

    def test_rect_y_64(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 2.5)

    def test_rect_y_65(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, None)

    def test_rect_y_66(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {})

    def test_rect_y_67(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, [])

    def test_rect_y_68(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, (1,))

    def test_rect_y_69(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, float("inf"))

    def test_rect_y_70(self):
        """A bad y raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, float("nan"))

    def test_rect_value_71(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rect_value_72(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rect_value_73(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rect_value_74(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rect_value_75(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rect_value_76(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rect_value_77(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-1, -2)

    def test_rect_value_78(self):
        """An out of range argument raises a ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 0)

    def test_rect_valid_79(self):
        """A valid rectangle is created."""
        self.assertIsInstance(Rectangle(1, 2), Rectangle)

    def test_rect_valid_80(self):
        """A valid rectangle is created."""
        self.assertIsInstance(Rectangle(1, 2, 3), Rectangle)

    def test_rect_valid_81(self):
        """A valid rectangle is created."""
        self.assertIsInstance(Rectangle(1, 2, 3, 4), Rectangle)

    def test_rect_valid_82(self):
        """A valid rectangle is created."""
        self.assertIsInstance(Rectangle(1, 2, 3, 4, 5), Rectangle)

    def test_rect_valid_83(self):
        """A valid rectangle is created."""
        self.assertIsInstance(Rectangle(10, 2), Rectangle)


class TestSaveToFileCases(unittest.TestCase):
    """Cover the save_to_file argument combinations."""

    def tearDown(self):
        """Remove the files created by the tests."""
        for name in ("Rectangle.json", "Square.json"):
            try:
                os.remove(name)
            except FileNotFoundError:
                pass

    def test_save_84(self):
        """Saving None writes an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_save_85(self):
        """Saving an empty list writes an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_save_86(self):
        """Saving None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_save_87(self):
        """Saving an empty list writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_save_88(self):
        """Saving one instance writes one dictionary."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as a_file:
            self.assertIn("id", a_file.read())

    def test_save_89(self):
        """Saving one instance writes one dictionary."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as a_file:
            self.assertIn("id", a_file.read())


if __name__ == "__main__":
    unittest.main()
