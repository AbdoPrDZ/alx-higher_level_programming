#!/usr/bin/python3
"""
10-square.py - This module defend an Square class inherits from Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square - the square class inherits from Rectangle class
    """

    def __init__(self, size):
        """
        __init__ - init square object

        Args:
            size (int): the square size
        """

        self.size = size

        super().__init__(self.size, self.size)

    @property
    def size(self):
        """
        size.getter - get the square size value

        Returns:
            int: the square size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        size.setter - set the square value

        Args:
            value (int): the square value
        """

        self.integer_validator("size", value)
        self.__size = value
