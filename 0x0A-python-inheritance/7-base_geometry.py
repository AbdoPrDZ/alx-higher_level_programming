#!/usr/bin/python3
"""
7-base_geometry.py - This module defend an BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry - Base Geometry class
    """

    def area(self):
        """
        area - is not implemented

        Raises:
            Exception: area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator - validate a integer value must be int

        Args:
            name (str): the name of value
            value (int): the value

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
