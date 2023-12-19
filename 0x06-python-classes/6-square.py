#!/usr/bin/python3
class Square:
    """
    Square - The square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ - Init square instance with size attribute

        Args:
            size (int, optional): The square size. Defaults to 0.
            position(tuple, optional): The square position. Defaults to (0, 0)

        Raises:
            TypeError: if size is not int
            ValueError: if size < 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif type(position) is not tuple\
                or len(position) != 2\
                or type(position[0]) is not int\
                or type(position[1]) is not int\
                or position[0] * position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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
        size.getter - Get the square size

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

    @property
    def position(self):
        """
        position.getter - Get the square position

        Return:
            int: The square position
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        position.setter - Set the square position

        Args:
            value (int): the square position

        Raises:
            TypeError: if position is not tuple of integers
        """
        if type(value) is not tuple\
                or len(value) != 2\
                or type(value[0]) is not int\
                or type(value[1]) is not int\
                or value[0] * value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """
        my_print - Print the square with # chars
        """
        import sys

        if self.size > 0:
            if self.position[1] > 0:
                print("\n" * self.position[1], end="", file=sys.stdout)

            for _ in range(self.size):
                print(" " * self.position[0], end="", file=sys.stdout)
                print("#" * self.size, file=sys.stdout)
        else:
            print(file=sys.stdout)
