#!/usr/bin/python3
"""
square.py - This module defines unittests for square class.

Unittest classes:
    TestSquare_instantiation - line 25
    TestSquare_size - line 97
    TestSquare_x - line 175
    TestSquare_y - line 249
    TestSquare_order_of_initialization - line 319
    TestSquare_area - line 337
    TestSquare_stdout - line 363
    TestSquare_update_args - line 464
    TestSquare_update_kwargs - line 599
    TestSquare_to_dictionary - line 722
"""

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """
    TestSquare_instantiation - testing instantiation of the Square class
    """

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        squareA = Square(10)
        squareB = Square(11)

        self.assertEqual(squareA.id, squareB.id - 1)

    def test_two_args(self):
        squareA = Square(10, 2)
        squareB = Square(2, 10)

        self.assertEqual(squareA.id, squareB.id - 1)

    def test_three_args(self):
        squareA = Square(10, 2, 2)
        squareB = Square(2, 2, 10)

        self.assertEqual(squareA.id, squareB.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        square = Square(4, 1, 9, 2)
        square.size = 8

        self.assertEqual(8, square.size)

    def test_width_getter(self):
        square = Square(4, 1, 9, 2)
        square.size = 8

        self.assertEqual(8, square.width)

    def test_height_getter(self):
        square = Square(4, 1, 9, 2)
        square.size = 8

        self.assertEqual(8, square.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquare_size(unittest.TestCase):
    """
    TestSquare_size - testing size initialization of the Square class
    """

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b"Python")

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b"abcdefg"))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b"abcdefg"))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float("inf"))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float("nan"))

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """
    TestSquare_x - testing initialization of Square x attribute
    """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b"Python")

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b"abcdefg"))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b"abcedfg"))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float("inf"), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float("nan"), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquare_y(unittest.TestCase):
    """
    TestSquare_y - testing initialization of Square y attribute
    """

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b"Python")

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b"abcdefg"))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b"abcedfg"))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float("inf"))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float("nan"))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquare_order_of_initialization(unittest.TestCase):
    """
    TestSquare_order_of_initialization - testing order of Square attribute initialization
    """

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
    """
    TestSquare_area - testing the area method of the Square class
    """

    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        square = Square(999999999999999999, 0, 0, 1)

        self.assertEqual(999999999999999998000000000000000001, square.area())

    def test_area_changed_attributes(self):
        square = Square(2, 0, 0, 1)
        square.size = 7

        self.assertEqual(49, square.area())

    def test_area_one_arg(self):
        square = Square(2, 10, 1, 1)

        with self.assertRaises(TypeError):
            square.area(1)


class TestSquare_stdout(unittest.TestCase):
    """
    TestSquare_stdout - testing __str__ and display methods of Square class
    """

    @staticmethod
    def capture_stdout(sq, method):
        """
        capture_stdout - captures and returns text printed to stdout

        Args:
            sq (Square): the Square ot print to stdout
            method (str): the method to run on sq
        Returns:
            str: the text printed to stdout by calling method on sq
        """

        capture = io.StringIO()

        sys.stdout = capture

        if method == "print":
            print(sq)
        else:
            sq.display()

        sys.stdout = sys.__stdout__

        return capture

    def test_str_method_print_size(self):
        square = Square(4)
        capture = TestSquare_stdout.capture_stdout(square, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(square.id)

        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        square = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(square.id)

        self.assertEqual(correct, square.__str__())

    def test_str_method_size_x_y(self):
        square = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(square.id)

        self.assertEqual(correct, str(square))

    def test_str_method_size_x_y_id(self):
        square = Square(2, 88, 4, 19)

        self.assertEqual("[Square] (19) 88/4 - 2", str(square))

    def test_str_method_changed_attributes(self):
        square = Square(7, 0, 0, [4])
        square.size = 15
        square.x = 8
        square.y = 10

        self.assertEqual("[Square] ([4]) 8/10 - 15", str(square))

    def test_str_method_one_arg(self):
        square = Square(1, 2, 3, 4)

        with self.assertRaises(TypeError):
            square.__str__(1)

    def test_display_size(self):
        square = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(square, "display")

        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        square = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(square, "display")

        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        square = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(square, "display")
        display = "\n####\n####\n####\n####\n"

        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        square = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(square, "display")
        display = "\n\n   ##\n   ##\n"

        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        square = Square(3, 4, 5, 2)

        with self.assertRaises(TypeError):
            square.display(1)


class TestSquare_update_args(unittest.TestCase):
    """
    TestSquare_update_args - testing update args method of the Square class
    """

    def test_update_args_zero(self):
        square = Square(10, 10, 10, 10)
        square.update()

        self.assertEqual("[Square] (10) 10/10 - 10", str(square))

    def test_update_args_one(self):
        square = Square(10, 10, 10, 10)
        square.update(89)

        self.assertEqual("[Square] (89) 10/10 - 10", str(square))

    def test_update_args_two(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2)

        self.assertEqual("[Square] (89) 10/10 - 2", str(square))

    def test_update_args_three(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3)

        self.assertEqual("[Square] (89) 3/10 - 2", str(square))

    def test_update_args_four(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4)

        self.assertEqual("[Square] (89) 3/4 - 2", str(square))

    def test_update_args_more_than_four(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4, 5)

        self.assertEqual("[Square] (89) 3/4 - 2", str(square))

    def test_update_args_width_setter(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2)

        self.assertEqual(2, square.width)

    def test_update_args_height_setter(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2)

        self.assertEqual(2, square.height)

    def test_update_args_None_id(self):
        square = Square(10, 10, 10, 10)
        square.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(square.id)

        self.assertEqual(correct, str(square))

    def test_update_args_None_id_and_more(self):
        square = Square(10, 10, 10, 10)
        square.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(square.id)

        self.assertEqual(correct, str(square))

    def test_update_args_twice(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4)
        square.update(4, 3, 2, 89)

        self.assertEqual("[Square] (4) 2/89 - 3", str(square))

    def test_update_args_invalid_size_type(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "invalid")

    def test_update_args_size_zero(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(89, 0)

    def test_update_args_size_negative(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(89, -4)

    def test_update_args_invalid_x(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(89, 1, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """
    TestSquare_update_kwargs - testing update kwargs method of Square class
    """

    def test_update_kwargs_one(self):
        square = Square(10, 10, 10, 10)
        square.update(id=1)

        self.assertEqual("[Square] (1) 10/10 - 10", str(square))

    def test_update_kwargs_two(self):
        square = Square(10, 10, 10, 10)
        square.update(size=1, id=2)

        self.assertEqual("[Square] (2) 10/10 - 1", str(square))

    def test_update_kwargs_three(self):
        square = Square(10, 10, 10, 10)
        square.update(y=1, size=3, id=89)

        self.assertEqual("[Square] (89) 10/1 - 3", str(square))

    def test_update_kwargs_four(self):
        square = Square(10, 10, 10, 10)
        square.update(id=89, x=1, y=3, size=4)

        self.assertEqual("[Square] (89) 1/3 - 4", str(square))

    def test_update_kwargs_width_setter(self):
        square = Square(10, 10, 10, 10)
        square.update(id=89, size=8)

        self.assertEqual(8, square.width)

    def test_update_kwargs_height_setter(self):
        square = Square(10, 10, 10, 10)
        square.update(id=89, size=9)

        self.assertEqual(9, square.height)

    def test_update_kwargs_None_id(self):
        square = Square(10, 10, 10, 10)
        square.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(square.id)

        self.assertEqual(correct, str(square))

    def test_update_kwargs_None_id_and_more(self):
        square = Square(10, 10, 10, 10)
        square.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(square.id)

        self.assertEqual(correct, str(square))

    def test_update_kwargs_twice(self):
        square = Square(10, 10, 10, 10)
        square.update(id=89, x=1)
        square.update(y=3, x=15, size=2)

        self.assertEqual("[Square] (89) 15/3 - 2", str(square))

    def test_update_kwargs_invalid_size(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=0)

    def test_update_kwargs_size_negative(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(y=-5)

    def test_update_args_and_kwargs(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2, y=6)

        self.assertEqual("[Square] (89) 10/10 - 2", str(square))

    def test_update_kwargs_wrong_keys(self):
        square = Square(10, 10, 10, 10)
        square.update(a=5, b=10)

        self.assertEqual("[Square] (10) 10/10 - 10", str(square))

    def test_update_kwargs_some_wrong_keys(self):
        square = Square(10, 10, 10, 10)
        square.update(size=5, id=89, a=1, b=54)

        self.assertEqual("[Square] (89) 10/10 - 5", str(square))


class TestSquare_to_dictionary(unittest.TestCase):
    """
    TestSquare_to_dictionary - testing to_dictionary method of the Square class
    """

    def test_to_dictionary_output(self):
        square = Square(10, 2, 1, 1)
        correct = {"id": 1, "x": 2, "size": 10, "y": 1}

        self.assertDictEqual(correct, square.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        squareA = Square(10, 2, 1, 2)
        squareB = Square(1, 2, 10)
        squareB.update(**squareA.to_dictionary())

        self.assertNotEqual(squareA, squareB)

    def test_to_dictionary_arg(self):
        square = Square(10, 10, 10, 10)

        with self.assertRaises(TypeError):
            square.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
