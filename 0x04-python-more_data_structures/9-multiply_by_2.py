#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dir_copy = a_dictionary.copy()
    list_keys = list(dir_copy.keys())

    for i in list_keys:
        dir_copy[i] *= 2

    return dir_copy
