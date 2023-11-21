#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    try:
        while i < list_length:
            try:
                elem = my_list_1[i] / my_list_2[i]
                new_list.append(elem)
                i += 1
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
                i += 1
            except (ValueError, TypeError):
                print("wrong type")
                new_list.append(0)
                i += 1
            except IndexError:
                print("out of range")
                new_list.append(0)
                break
    finally:
        return new_list
