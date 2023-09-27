#!/usr/bin/python3

"""Definition of class Square"""


class Square:
    """Constractor of the square."""
    def __init__(self, size=0):
        """Initialize the attr.

        args:
            size (int): the size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """function to calculate the area of the square"""
        return self.__size ** 2