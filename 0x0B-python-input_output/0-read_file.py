#!/usr/bin/python3

"""
This module defines a function read_file(...)
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:
    args:
        filename(str): name of file

    """
    with open(filename, "r", encoding="UTF8") as file:
        buffer = file.read()
        print(buffer)
