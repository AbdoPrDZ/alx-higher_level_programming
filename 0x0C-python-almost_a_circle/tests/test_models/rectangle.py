#!/usr/bin/python3
"""
rectangle.py - This module defines unittests for rectangle class

Unittest classes:
    TestRectangle_instantiation - line 26
    TestRectangle_width - line 128
    TestRectangle_height - line 206
    TestRectangle_x - line 280
    TestRectangle_y - line 354
    TestRectangle_order_of_initialization - line 424
    TestRectangle_area - line 455
    TestRectangle_stdout - line 484
    TestRectangle_update_args - line 582
    TestRectangle_update_kwargs - line 746
    TestRectangle_to_dictionary - line 881
"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """
    TestRectangle_instantiation - testing instantiation of the Rectangle class
    """

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        rectangleA = Rectangle(10, 2)
        rectangleB = Rectangle(2, 10)

        self.assertEqual(rectangleA.id, rectangleB.id - 1)

    def test_three_args(self):
        rectangleA = Rectangle(2, 2, 4)
        rectangleB = Rectangle(4, 4, 2)

        self.assertEqual(rectangleA.id, rectangleB.id - 1)

    def test_four_args(self):
        rectangleA = Rectangle(1, 2, 3, 4)
        rectangleB = Rectangle(4, 3, 2, 1)

        self.assertEqual(rectangleA.id, rectangleB.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)

        self.assertEqual(5, rectangle.width)

    def test_width_setter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)
        rectangle.width = 10

        self.assertEqual(10, rectangle.width)

    def test_height_getter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)

        self.assertEqual(7, rectangle.height)

    def test_height_setter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)
        rectangle.height = 10

        self.assertEqual(10, rectangle.height)

    def test_x_getter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)

        self.assertEqual(7, rectangle.x)

    def test_x_setter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)
        rectangle.x = 10

        self.assertEqual(10, rectangle.x)

    def test_y_getter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)

        self.assertEqual(5, rectangle.y)

    def test_y_setter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)
        rectangle.y = 10

        self.assertEqual(10, rectangle.y)


class TestRectangle_width(unittest.TestCase):
    """
    TestRectangle_width - testing initialization of Rectangle width attribute
    """

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"Python", 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b"Abdo Pr"), 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b"Abdo Pr"), 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("inf"), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("nan"), 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """
    TestRectangle_height - testing initialization of Rectangle height attribute
    """

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b"Python")

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b"Abdo Pr"))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b"Abdo Pr"))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("inf"))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("nan"))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """
    TestRectangle_x - testing initialization of Rectangle x attribute
    """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b"Python")

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b"Abdo Pr"))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b"Abdo Pr"))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float("inf"), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float("nan"), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """
    TestRectangle_y - testing initialization of Rectangle y attribute
    """

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b"Python")

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b"Abdo Pr"))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b"Abdo Pr"))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float("inf"))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float("nan"))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """
    TestRectangle_order_of_initialization - testing Rectangle order
                                            of attribute initialization
    """

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """
    TestRectangle_area - testing the area method of the Rectangle class
    """

    def test_area_small(self):
        rectangle = Rectangle(10, 2, 0, 0, 0)

        self.assertEqual(20, rectangle.area())

    def test_area_large(self):
        rectangle = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)

        self.assertEqual(999999999999998999000000000000001, rectangle.area())

    def test_area_changed_attributes(self):
        rectangle = Rectangle(2, 10, 1, 1, 1)
        rectangle.width = 7
        rectangle.height = 14

        self.assertEqual(98, rectangle.area())

    def test_area_one_arg(self):
        rectangle = Rectangle(2, 10, 1, 1, 1)

        with self.assertRaises(TypeError):
            rectangle.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """
    TestRectangle_stdout - testing __str__ and display methods of Rectangle class
    """

    @staticmethod
    def capture_stdout(rect, method):
        """
        capture_stdout - captures and returns text printed to stdout

        Args:
            rect (Rectangle): the Rectangle to print to stdout
            method (str): the method to run on rect.
        Returns:
            str: the text printed to stdout by calling method on sq
        """

        capture = io.StringIO()
        sys.stdout = capture

        if method == "print":
            print(rect)
        else:
            rect.display()

        sys.stdout = sys.__stdout__

        return capture

    def test_str_method_print_width_height(self):
        rectangle = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(rectangle, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(rectangle.id)

        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        rectangle = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(rectangle.id)

        self.assertEqual(correct, rectangle.__str__())

    def test_str_method_width_height_x_y(self):
        rectangle = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(rectangle.id)

        self.assertEqual(correct, str(rectangle))

    def test_str_method_width_height_x_y_id(self):
        rectangle = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rectangle))

    def test_str_method_changed_attributes(self):
        rectangle = Rectangle(7, 7, 0, 0, [4])
        rectangle.width = 15
        rectangle.height = 1
        rectangle.x = 8
        rectangle.y = 10

        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rectangle))

    def test_str_method_one_arg(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rectangle.__str__(1)

    def test_display_width_height(self):
        rectangle = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(rectangle, "display")

        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        rectangle = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(rectangle, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        rectangle = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(rectangle, "display")
        display = "\n####\n####\n####\n####\n####\n"

        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        rectangle = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(rectangle, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"

        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        rectangle = Rectangle(5, 1, 2, 4, 7)

        with self.assertRaises(TypeError):
            rectangle.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """
    TestRectangle_update_args - testing update args method of the Rectangle class
    """

    def test_update_args_zero(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update()

        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rectangle))

    def test_update_args_one(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89)

        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rectangle))

    def test_update_args_two(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2)

        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rectangle))

    def test_update_args_three(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2, 3)

        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rectangle))

    def test_update_args_four(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4)

        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rectangle))

    def test_update_args_five(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4, 5)

        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rectangle))

    def test_update_args_more_than_five(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4, 5, 6)

        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rectangle))

    def test_update_args_None_id(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(rectangle.id)

        self.assertEqual(correct, str(rectangle))

    def test_update_args_None_id_and_more(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(rectangle.id)

        self.assertEqual(correct, str(rectangle))

    def test_update_args_twice(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4, 5, 6)
        rectangle.update(6, 5, 4, 3, 2, 89)

        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rectangle))

    def test_update_args_invalid_width_type(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "invalid")

    def test_update_args_width_zero(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(89, 0)

    def test_update_args_width_negative(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(89, -5)

    def test_update_args_invalid_height_type(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(89, 1, 0)

    def test_update_args_height_negative(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """
    TestRectangle_update_kwargs - testing update kwargs method of the Rectangle class
    """

    def test_update_kwargs_one(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=1)

        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rectangle))

    def test_update_kwargs_two(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(width=2, id=1)

        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rectangle))

    def test_update_kwargs_three(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(width=2, height=3, id=89)

        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rectangle))

    def test_update_kwargs_four(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=89, x=1, height=2, y=3, width=4)

        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(rectangle))

    def test_update_kwargs_five(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(y=5, x=8, id=99, width=1, height=2)

        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(rectangle))

    def test_update_kwargs_None_id(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(rectangle.id)

        self.assertEqual(correct, str(rectangle))

    def test_update_kwargs_None_id_and_more(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(rectangle.id)

        self.assertEqual(correct, str(rectangle))

    def test_update_kwargs_twice(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=89, x=1, height=2)
        rectangle.update(y=3, height=15, width=2)

        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(rectangle))

    def test_update_kwargs_invalid_width_type(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(width=0)

    def test_update_kwargs_width_negative(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(height=0)

    def test_update_kwargs_height_negative(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle.update(y=-5)

    def test_update_args_and_kwargs(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2, height=4, y=6)

        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rectangle))

    def test_update_kwargs_wrong_keys(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(a=5, b=10)

        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rectangle))

    def test_update_kwargs_some_wrong_keys(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(height=5, id=89, a=1, b=54, x=19, y=7)

        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(rectangle))


class TestRectangle_to_dictionary(unittest.TestCase):
    """
    TestRectangle_to_dictionary - testing to_dictionary method of the Rectangle class
    """

    def test_to_dictionary_output(self):
        rectangle = Rectangle(10, 2, 1, 9, 5)
        correct = {"x": 1, "y": 9, "id": 5, "height": 2, "width": 10}

        self.assertDictEqual(correct, rectangle.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        rectangleA = Rectangle(10, 2, 1, 9, 5)
        rectangleB = Rectangle(5, 9, 1, 2, 10)
        rectangleB.update(**rectangleA.to_dictionary())

        self.assertNotEqual(rectangleA, rectangleB)

    def test_to_dictionary_arg(self):
        rectangle = Rectangle(10, 2, 4, 1, 2)

        with self.assertRaises(TypeError):
            rectangle.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
