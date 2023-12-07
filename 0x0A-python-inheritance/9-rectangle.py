#!/usr/bin/python3
"""This module defines a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """define a class Rectangle"""

    def __init__(self, width, height):
        """Initialize the attribute of the object
        args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Return the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
