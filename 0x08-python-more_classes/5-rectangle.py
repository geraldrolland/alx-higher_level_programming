#!/usr/bin/python3

"""
This is module docstring for 5-rectangle

This defines the class Rectangle
"""


class Rectangle:
    """Defines the class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the attribute of the objects.
        args:
            width(int): width of Rectangle
            height(int): height of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the object"""
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]  # Remove the last newline

    def __del__(self):
        print("Bye rectangle...")

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
