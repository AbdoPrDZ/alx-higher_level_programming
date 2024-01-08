#!/usr/bin/python3

"""
8-rectangle - This module defend an Rectangle class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle - rectangle class that receive width and height as parameters
    """

    def __init__(self, width, height):
        """
        __init__ - validate and create Rectangle object

        Args:
            width (int): the rectangle width
            height (int): the rectangle height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
