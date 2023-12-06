#!/usr/bin/python3


"""
This module defines the function append_write(...)
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    args:
        filename(str): name of file
        text(str): buffer to write
    """
    with open(filename, "a", encoding="UTF8") as file:
        num_byte = file.write(text)
        return num_byte
