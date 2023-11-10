#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list_copy = my_list.copy()
    i = 0
    for elem in my_list_copy:
        if elem == search:
            my_list_copy[i] = replace
            i += 1
            continue
        i += 1
        continue
    return my_list_copy
