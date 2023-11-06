#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_copy = my_list.copy()
    if idx > len(my_list) - 1 or idx < 0:
        return my_list_copy
    for elem in my_list_copy:
        if elem == my_list_copy[idx]:
            my_list_copy[idx] = element
            return my_list_copy
        continue
