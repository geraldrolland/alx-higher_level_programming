#!/usr/bin/python3

""""Define a class Square"""


class Square:
    """""Represent a Square."""""

    def __init__(self, size=0, position=(0, 0)):
        """""Initialize a New Square.
        Args:
            size(int): The size of the Square
            position(tuple): The position of the cordinate
        """""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (len(position) != 2 or
              not all(isinstance(elem, int) for elem in position) or
              not all(elem >= 0 for elem in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """"The area() method Return the area of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """"Get the position of a Square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (len(value) != 2 or
                not all(isinstance(elem, int) for elem in value) or
                not all(elem >= 0 for elem in value)):
            self.__position[0] = value[0]
            self.__position[1] = value[1]

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
            print(self.__position[0] * "_", end="")
            while j < self.size:
                print("#", end="")
                j += 1
            i += 1
            print()
