#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first and second elements from each tuple, using 0 if missing
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    # Calculate the sum of corresponding elements
    sum_1 = a1 + b1
    sum_2 = a2 + b2

    # Return a new tuple with the sums
    return (sum_1, sum_2)
