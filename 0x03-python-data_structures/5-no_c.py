#!/usr/bin/env python3
def no_c(my_string):
    j = 0
    for i in my_string:
        if i == "C" or i == "c":
            my_string = my_string[:j] + my_string[j+1:]
            continue
        j += 1
    return my_string
