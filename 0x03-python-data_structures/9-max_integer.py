#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    for elem in my_list:
        if elem == my_list[0]:
            continue
        elif my_list[0] < elem:
            my_list[0] = elem
            continue
        continue
    return my_list[0]
