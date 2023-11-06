#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list == []:
        print()
    for elem in my_list:
        txt = "{:d}"
        print(txt.format(elem))
