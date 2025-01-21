#!/usr/bin/python3

def max_integer(my_list=[]):
    i = 0
    max = 0

    if my_list is None:
        return None

    while i < len(my_list):
        if my_list[i] > max:
            max = my_list[i]
        else:
            i += 1
    return max
