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

    @property
    def size(self):
        """
        size - Get the square size

        Return:
            int: The square size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        size.setter - Set the square size

        Args:
            value (int): the square size

        Raises:
            TypeError: if size is not int
            ValueError: if size < 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __eq__(self, other):
        """
        __eq__ - Compare if this square is equal than the other

        Args:
            other (Square): The other square

        Return:
            bool: this square is equals the other or not
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        __ne__ - Compare if this square is different than the other

        Args:
            other (Square): The other square

        Return:
            bool: this square is not equals the other or not
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        __gt__ - Compare if this square is greater than the other

        Args:
            other (Square): The other square

        Return:
            bool: this square is greaten than other or not
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        __ge__ - Compare if this square is less than the other

        Args:
            other (Square): The other square

        Return:
            bool: this square is greaten than or equals other or not
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        __lt__ - Compare if this square is less than the other

        Args:
            other (Square): The other square

        Return:
            bool: this square is less than other or not
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        __le__ - Compare if this square is less ot equal than the other

        Args:
            other (Square): The other square

        Return:
            bool: this square is less than or equals other or not
        """
        return self.area() <= other.area()
