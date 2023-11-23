#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """""Initialize a New Squaere.
        Args:
            size(int): size of the new Square
        """""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Get / set the current size of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        """"The area() method Return the area of the Square"""
        return self.__size ** 2

    def my_print(self):
        """"print the square with character #"""
        if self.__size == 0:
            print()
        i = 0
        while i < self.__size:
            j = 0
            while j < self.size:
                print("#", end="")
                j += 1
            i += 1
            print()
