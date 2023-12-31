#!/usr/bin/python3
"""
Square Class
"""


class Square:
    """
    Square - The square class
    """

    def __init__(self, size=0):
        """
        __init__ - Init square instance with size attribute

        Args:
            size (int, optional): The square size. Defaults to 0.

        Raises:
            TypeError: if size is not int
            ValueError: if size < 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        area - Get the square area

        Returns:
            int: The square area
        """
        return self.__size * self.__size
