#!/usr/bin/python3
"""
Rectangle class with width and hight properties
"""


class Rectangle:
    """
    Rectangle - rectangle with width and height
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        __init__ - init the rectangle instance

        Args:
            width (int, optional): the rectangle width. Defaults to 0.
            height (int, optional): the rectangle height. Defaults to 0.
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
        """width.setter - set the rectangle width

        Args:
            value (int): the rectangle width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

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
        """height.setter - set the rectangle height

        Args:
            value (int): the rectangle height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        area - get the rectangle area

        Returns:
            int: the rectangle area
        """

        return self.width * self.height

    def perimeter(self):
        """
        perimeter - get the rectangle perimeter

        Returns:
            int: the rectangle perimeter
        """

        if self.width > 0 and self.height > 0:
            return self.width * 2 + self.height * 2
        return 0

    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal - get the bigger rectangle between two rectangles

        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle

        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_2 must be an instance of Rectangle

        Returns:
            Rectangle: the bigger rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """
        __str__ - get the rectangle string

        Returns:
            str: the rectangle string
        """

        _str = ""

        if self.width > 0 and self.height > 0:
            row = ("{}".format(self.print_symbol) * self.width) + "\n"
            _str = (row * self.height)[:-1]

        return _str

    def __repr__(self):
        """
        __repr__ - get the rectangle represent string

        Returns:
            str: the rectangle represent string
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        __del__ - print bye message on instance deleted
        """

        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
