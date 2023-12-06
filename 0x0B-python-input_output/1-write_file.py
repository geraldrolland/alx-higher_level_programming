#!/usr/bin/python3


"""
This module defines a function write_file(...)
"""


def write_file(filename="", text=""):
    """writes a string to a text file
    args:
        filename(str): name of file
        text(str): bytes to write
    """
    with open(filename, "w", encoding="UTF8") as file:

        num_bytes = file.write(text)
        return num_bytes
