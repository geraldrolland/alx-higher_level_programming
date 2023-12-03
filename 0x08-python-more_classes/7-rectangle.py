#!/usr/bin/python3


"""
This is the module docstring for 7-rectangle

This module defines a class Rectangle
"""


class Rectangle:
    """Defines a class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the attributes of the objects.
        args:
            width(int): width of the object
            height(int): height of the object
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str[:-1]  # Remove the last newline

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
