#!/usr/bin/python3

"""Definition of class Square"""


class Square:
    """Constractor of class square."""
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

    @property
    def size(self):
        """getter for size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for the size with a setter

        args:
            value (int): the value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """function to calculate the area of the square"""
        return self.__size ** 2
