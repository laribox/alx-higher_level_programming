#!/usr/bin/python3

"""Definition of class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """init that data of Square.

        args:
            size (int): the size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
