#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """function that prints an integer with "{:d}".format().

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    counter = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (counter)