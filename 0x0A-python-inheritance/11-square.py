#!/usr/bin/python3
"""This module defines a class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square"""

    def __init__(self, size):
        """Initialize the attribute of the object.
        args:
            size(int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
