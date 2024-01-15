#!/usr/bin/python3
"""
rectangle.py - This module defined a Rectangle class inherits from Base class
"""

from models.base import Base


class Rectangle(Base):

    """
    Rectangle - the Rectangle class inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ - create the Rectangle instance

        Args:
            width (int): the rectangle width
            height (int): the rectangle height
            x (int, optional): the rectangle pos in x axis. Defaults to 0.
            y (int, optional): the rectangle pos in x axis. Defaults to 0.
            id (int, optional): the rectangle id. Defaults to None.
        """

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        area - get the rectangle area

        Returns:
            int: the rectangle area
        """

        return self.width * self.height

    def display(self):
        """
        display - print the rectangle using the character #
        """

        _str = ""

        if self.width > 0 and self.height > 0:
            row = (" " * self.x) + ("#" * self.width) + "\n"
            _str = ("\n" * self.y) + (row * self.height)[:-1]

        print(_str)

    def update(self, *args, **kwargs):
        """
        update - update the instance attributes

        Args:
            args (list): the no-keyword arguments of new values
            kwargs (dict): the key-worded arguments of new values
        """

        args_len = len(args)

        if not args_len == 0:
            self.id = args[0] if args_len >= 1 else self.id
            self.width = args[1] if args_len >= 2 else self.width
            self.height = args[2] if args_len >= 3 else self.height
            self.x = args[3] if args_len >= 4 else self.x
            self.y = args[4] if args_len >= 5 else self.y
        else:
            self.id = kwargs["id"] if "id" in kwargs.keys() else self.id
            if "width" in kwargs.keys():
                self.width = kwargs["width"]
            if "height" in kwargs.keys():
                self.height = kwargs["height"]
            self.x = kwargs["x"] if "x" in kwargs.keys() else self.x
            self.y = kwargs["y"] if "y" in kwargs.keys() else self.y

    def to_dictionary(self):
        """
        to_dictionary - get the dict of all attributes

        Returns:
            dict: the dict of all attributes
        """

        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }

    @property
    def width(self):
        """
        width.getter - get the rectangle width

        Returns:
            int: the rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        width.setter - set the rectangle width

        Args:
            value (int): the rectangle width
        """

        if not (type(value) is int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        height.getter - get the rectangle height

        Returns:
            int: the rectangle height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        height.setter - set the rectangle height

        Args:
            value (int): the rectangle height
        """

        if not (type(value) is int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        x.getter - get the rectangle pos in x axis

        Returns:
            int: the rectangle pos in x axis
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        x.setter - set the rectangle pos in x axis

        Args:
            value (int): the rectangle pos in x axis
        """

        if not (type(value) is int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        y.getter - get the rectangle pos in y axis

        Returns:
            int: the rectangle pos in y axis
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        y.setter - set the rectangle pos in y axis

        Args:
            value (int): the rectangle pos in y axis
        """

        if not (type(value) is int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def __str__(self):
        """
        __str__ - get the rectangle string

        Returns:
            str: the rectangle string
        """

        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(
            self.id, self.x, self.y, self.width, self.height
        )
