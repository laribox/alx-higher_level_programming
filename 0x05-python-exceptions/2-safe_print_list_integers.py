#!/usr/bin/python3

"""function that prints the first x elements of a list and only integers."""


def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            counter += 1
        except(ValueError, TypeError):
            continue
    print()
    return counter
