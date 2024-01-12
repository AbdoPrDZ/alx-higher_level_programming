#!/usr/bin/python3
"""
base.py - This module defines unittests for Base class

Unittest classes:
    TestBase_instantiation - line 21
    TestBase_to_json_string - line 208
    TestBase_save_to_file - line 320
    TestBase_from_json_string - line 454
    TestBase_create - line 551
    TestBase_load_from_file - line 645
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """
    TestBase_instantiation - testing instantiation of the Base class
    """

    def test_no_arg(self):
        """
        test_no_arg - test create base instance with no args
        """

        baseA = Base()
        baseB = Base()

        self.assertEqual(baseA.id, baseB.id - 1)

    def test_three_bases(self):
        """
        test_three_bases - test create third instances of base
        """

        baseA = Base()
        baseB = Base()
        baseC = Base()

        self.assertEqual(baseA.id, baseC.id - 2)

    def test_None_id(self):
        """
        test_None_id - test create base instance with None as a id
        """

        baseA = Base(None)
        baseB = Base(None)

        self.assertEqual(baseA.id, baseB.id - 1)

    def test_unique_id(self):
        """
        test_unique_id - test unique ids of base instances
        """

        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        """
        test_nb_instances_after_unique_id - test nb_instances after unique ids
        """

        baseA = Base()
        baseB = Base(12)
        baseC = Base()

        self.assertEqual(baseA.id, baseC.id - 1)

    def test_id_public(self):
        """
        test_id_public - test change id of base instance from public
        """

        base = Base(12)
        base.id = 15

        self.assertEqual(15, base.id)

    def test_nb_instances_private(self):
        """
        test_nb_instances_private - test get __nb_instances private
                                    of base instance
        """

        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        """
        test_str_id - test create base instance with string as a id
        """

        self.assertEqual("Abdo Pr", Base("Abdo Pr").id)

    def test_float_id(self):
        """
        test_float_id - set set the id as a float as a id
        """

        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        """
        test_complex_id - test create base instance with complex as a id
        """

        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        """
        test_dict_id - test create base instance with dictionary as a id
        """

        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        """
        test_bool_id - test create base instance with boolean as a id
        """

        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """
        test_list_id - test create base instance with list as a id
        """

        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        """
        test_tuple_id - test create base instance with tuple as a id
        """

        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        """
        test_set_id - test create base instance with set as a id
        """

        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        """
        test_frozenset_id - test create base instance with frozenset as a id
        """

        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        """
        test_range_id - test create base instance with range as a id
        """

        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        """
        test_bytes_id - test create base instance with bytes as a id
        """

        self.assertEqual(b"Python", Base(b"Python").id)

    def test_bytearray_id(self):
        """
        test_bytearray_id - test create base instance with bytearray as a id
        """

        self.assertEqual(bytearray(b"abcefg"), Base(bytearray(b"abcefg")).id)

    def test_memoryview_id(self):
        """
        test_memoryview_id - test create base instance with memoryview as a id
        """

        self.assertEqual(memoryview(b"abcefg"), Base(memoryview(b"abcefg")).id)

    def test_inf_id(self):
        """
        test_inf_id - test create base instance with inf float as a id
        """

        self.assertEqual(float("inf"), Base(float("inf")).id)

    def test_NaN_id(self):
        """
        test_NaN_id - test create base instance with NaN as a id
        """

        self.assertNotEqual(float("nan"), Base(float("nan")).id)

    def test_two_args(self):
        """
        test_two_args - test create base instance with two args
        """

        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """
    TestBase_to_json_string - testing to_json_string function of Base class
    """

    def test_to_json_string_rectangle_type(self):
        """
        test_to_json_string_rectangle_type - testing the type of
                                            test_to_json_string function return
                                            of rectangle class
        """

        rectangle = Rectangle(10, 7, 2, 8, 6)

        self.assertEqual(str, type(Base.to_json_string([rectangle.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        """
        test_to_json_string_rectangle_one_dict - testing one dict of
                                                to_json_string function
                                                of rectangle class
        """

        rectangle = Rectangle(10, 7, 2, 8, 6)

        self.assertTrue(len(Base.to_json_string([rectangle.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        """
        test_to_json_string_rectangle_two_dicts - testing two dicts of
                                                to_json_string function
                                                of rectangle class
        """

        rectangleA = Rectangle(2, 3, 5, 19, 2)
        rectangleB = Rectangle(4, 2, 4, 1, 12)

        dicts = [rectangleA.to_dictionary(), rectangleB.to_dictionary()]

        self.assertTrue(len(Base.to_json_string(dicts)) == 106)

    def test_to_json_string_square_type(self):
        """
        test_to_json_string_square_type - testing the return type of
                                        to_json_string function
                                        of class square
        """

        square = Square(10, 2, 3, 4)

        self.assertEqual(str, type(Base.to_json_string([square.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        """
        test_to_json_string_square_one_dict - testing one dict of
                                            to_json_string function
                                            of class square
        """

        squre = Square(10, 2, 3, 4)

        self.assertTrue(len(Base.to_json_string([squre.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        """
        test_to_json_string_square_two_dicts - testing two dicts of
                                            to_json_string function
                                            of class square
        """

        squareA = Square(10, 2, 3, 4)
        squareB = Square(4, 5, 21, 2)

        dicts = [squareA.to_dictionary(), squareB.to_dictionary()]

        self.assertTrue(len(Base.to_json_string(dicts)) == 78)

    def test_to_json_string_empty_list(self):
        """
        test_to_json_string_empty_list - test pass empty list to
                                         to_json_string function
        """

        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        """
        test_to_json_string_none - test pass none to
                                   to_json_string function
        """

        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """
        test_to_json_string_no_args - test pass no args to
                                      to_json_string function
        """

        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        """
        test_to_json_string_more_than_one_arg - test pass more to
                                                to_json_string function
        """

        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """
    TestBase_save_to_file - testing save_to_file function of Base class
    """

    @classmethod
    def tearDown(self):
        """
        tearDown - remove the files created
        """

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        if os.path.exists("Base.json"):
            os.remove("Base.json")

    def test_save_to_file_one_rectangle(self):
        """
        test_save_to_file_one_rectangle - testing saving to file of one
                                          rectangle instance
        """

        rectangle = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rectangle])

        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        """
        test_save_to_file_two_rectangles - testing saving to file of two
                                           rectangles instances
        """

        rectangleA = Rectangle(10, 7, 2, 8, 5)
        rectangleB = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rectangleA, rectangleB])

        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        """
        test_save_to_file_one_square - testing saving to file of one
                                       square instance
        """

        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])

        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        """
        test_save_to_file_two_squares - testing saving to file of two
                                        squares instances
        """

        squareA = Square(10, 7, 2, 8)
        squareB = Square(8, 1, 2, 3)
        Square.save_to_file([squareA, squareB])

        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        """
        test_save_to_file_cls_name_for_filename - testing saving to file using cls
                                                  name for filename
        """

        square = Square(10, 7, 2, 8)
        Base.save_to_file([square])

        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        """
        test_save_to_file_overwrite - testing saving to existing file
        """

        square = Square(9, 2, 39, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])

        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        """
        test_save_to_file_None - testing pass none to save_to_file function
        """

        Square.save_to_file(None)

        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        """
        test_save_to_file_empty_list - testing saving empty list
        """

        Square.save_to_file([])

        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        """
        test_save_to_file_no_args - test pass no args to save_to_file
                                    of rectangle class
        """

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        """
        test_save_to_file_more_than_one_arg - test pass more args to save_to_file
                                              of square class
        """

        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """
    TestBase_from_json_string - testing from_json_string function of Base class
    """

    def test_from_json_string_type(self):
        """
        test_from_json_string_type - testing from_json_string function return type
                                    of class rectangle
        """

        inputs = [{"id": 89, "width": 10, "height": 4}]
        json_string = Rectangle.to_json_string(inputs)
        outputs = Rectangle.from_json_string(json_string)

        self.assertEqual(list, type(outputs))

    def test_from_json_string_one_rectangle(self):
        """
        test_from_json_string_one_rectangle - testing on rectangle
        """

        inputs = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_string = Rectangle.to_json_string(inputs)
        outputs = Rectangle.from_json_string(json_string)

        self.assertEqual(inputs, outputs)

    def test_from_json_string_two_rectangles(self):
        """
        test_from_json_string_two_rectangles - testing two rectangles
        """

        inputs = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_string = Rectangle.to_json_string(inputs)
        outputs = Rectangle.from_json_string(json_string)

        self.assertEqual(inputs, outputs)

    def test_from_json_string_one_square(self):
        """
        test_from_json_string_one_square - testing on square
        """

        inputs = [{"id": 89, "size": 10, "height": 4}]
        json_string = Square.to_json_string(inputs)
        outputs = Square.from_json_string(json_string)

        self.assertEqual(inputs, outputs)

    def test_from_json_string_two_squares(self):
        """
        test_from_json_string_two_squares - testing two squares
        """

        inputs = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7},
        ]
        json_string = Square.to_json_string(inputs)
        outputs = Square.from_json_string(json_string)

        self.assertEqual(inputs, outputs)

    def test_from_json_string_None(self):
        """
        test_from_json_string_None - testing None as argument
        """
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        """
        test_from_json_string_empty_list - testing empty list as argument
        """

        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """
        test_from_json_string_no_args - testing no args
        """

        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """
        test_from_json_string_more_than_one_arg - testing more args
        """

        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """
    TestBase_create - testing create function of Base class
    """

    def test_create_rectangle_original(self):
        """
        test_create_rectangle_original - testing original
        """

        rectangleA = Rectangle(3, 5, 1, 2, 7)
        dictA = rectangleA.to_dictionary()
        rectangleB = Rectangle.create(**dictA)

        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rectangleA))

    def test_create_rectangle_new(self):
        """
        test_create_rectangle_new - testing new
        """

        rectangleA = Rectangle(3, 5, 1, 2, 7)
        dictA = rectangleA.to_dictionary()
        rectangleB = Rectangle.create(**dictA)

        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rectangleB))

    def test_create_rectangle_is(self):
        """
        test_create_rectangle_is - testing is
        """

        rectangleA = Rectangle(3, 5, 1, 2, 7)
        dictA = rectangleA.to_dictionary()
        rectangleB = Rectangle.create(**dictA)

        self.assertIsNot(rectangleA, rectangleB)

    def test_create_rectangle_equals(self):
        """
        test_create_rectangle_equals - testing equals
        """

        rectangleA = Rectangle(3, 5, 1, 2, 7)
        dictA = rectangleA.to_dictionary()
        rectangleB = Rectangle.create(**dictA)

        self.assertNotEqual(rectangleA, rectangleB)

    def test_create_square_original(self):
        """
        test_create_square_original - testing original
        """

        squareA = Square(3, 5, 1, 7)
        dictA = squareA.to_dictionary()
        squareB = Square.create(**dictA)

        self.assertEqual("[Square] (7) 5/1 - 3", str(squareA))

    def test_create_square_new(self):
        """
        test_create_square_new - testing new
        """

        squareA = Square(3, 5, 1, 7)
        dictA = squareA.to_dictionary()
        squareB = Square.create(**dictA)

        self.assertEqual("[Square] (7) 5/1 - 3", str(squareB))

    def test_create_square_is(self):
        """
        test_create_square_is - testing is
        """

        squareA = Square(3, 5, 1, 7)
        dictA = squareA.to_dictionary()
        squareB = Square.create(**dictA)

        self.assertIsNot(squareA, squareB)

    def test_create_square_equals(self):
        """
        test_create_square_equals - testing equals
        """

        squareA = Square(3, 5, 1, 7)
        dictA = squareA.to_dictionary()
        squareB = Square.create(**dictA)

        self.assertNotEqual(squareA, squareB)


class TestBase_load_from_file(unittest.TestCase):
    """
    TestBase_load_from_file - testing load_from_file_method of Base class
    """

    @classmethod
    def tearDown(self):
        """
        tearDown - remove the files created
        """

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_load_from_file_first_rectangle(self):
        """
        test_load_from_file_first_rectangle - testing first rectangle
        """

        rectangleA = Rectangle(10, 7, 2, 8, 1)
        rectangleB = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangleA, rectangleB])

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(str(rectangleA), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        """
        test_load_from_file_second_rectangle - testing second rectangle
        """

        rectangleA = Rectangle(10, 7, 2, 8, 1)
        rectangleB = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangleA, rectangleB])

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(str(rectangleB), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        """
        test_load_from_file_rectangle_types - testing rectangle types
        """

        rectangleA = Rectangle(10, 7, 2, 8, 1)
        rectangleB = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangleA, rectangleB])

        output = Rectangle.load_from_file()

        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        """
        test_load_from_file_first_square - testing first square
        """

        squareA = Square(5, 1, 3, 3)
        squareB = Square(9, 5, 2, 3)
        Square.save_to_file([squareA, squareB])

        list_squares_output = Square.load_from_file()

        self.assertEqual(str(squareA), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        """
        test_load_from_file_second_square - testing second square
        """

        squareA = Square(5, 1, 3, 3)
        squareB = Square(9, 5, 2, 3)
        Square.save_to_file([squareA, squareB])

        list_squares_output = Square.load_from_file()

        self.assertEqual(str(squareB), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        """
        test_load_from_file_square_types - testing square types
        """

        squareA = Square(5, 1, 3, 3)
        squareB = Square(9, 5, 2, 3)
        Square.save_to_file([squareA, squareB])

        output = Square.load_from_file()

        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        """
        test_load_from_file_no_file - testing no file
        """

        output = Square.load_from_file()

        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        """
        test_load_from_file_more_than_one_arg - testing more args
        """

        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
