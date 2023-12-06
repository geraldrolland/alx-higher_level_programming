#!/usr/bin/python3


"""
This module provide the function append_after(...)
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,.
    args:
        filename(str): file name
        search_string(str): search string
        new_string(str): new string to insert
    """
    try:
        with open(filename, "r+", encoding="UTF8") as file:
            lines = file.readlines()
            if lines == []:
                file.write(new_string)
                return
            my_list = []
            for line in lines:
                my_list.append(line)
        with open(filename, "w", encoding="UTF8") as file:
            for lines in my_list:
                file.write(lines)
                line_split = lines.split()
                for word in line_split:
                    if search_string in word:
                        if "\n" not in new_string:
                            new_string += "\n"
                        file.write(new_string)
                    continue
                continue
    except FileNotFoundError:
        with open(filename, "w", encoding="UTF8") as file:
            file.write(new_string)
