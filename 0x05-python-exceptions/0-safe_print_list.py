#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list == []:
        return 0
    try:
        i = 0
        while i < x:
            print("{:d}".format(my_list[i]), end="")
            i += 1
    except IndexError:
        print()
        return i
    else:
        print()
        return i
