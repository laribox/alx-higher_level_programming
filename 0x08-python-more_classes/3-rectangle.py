#!/usr/bin/python3
""" this class represent the Rectangle with width and height and some functions"""


class Rectangle:
    """private attributes width and height"""
    def __init__(self, width=0, height=0):
        """instanciates the class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate and the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate and returns the perimeter of the rectangle"""
        perimeter = 0
        if self.__height == 0 or self.__width == 0:
            return perimeter
        else:
            perimeter = (self.__height + self.__width) * 2
            return perimeter

    def __str__(self):
        """returns a rectangle shape using '#'"""
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            rectangle = ""
        else:
            for i in range(self.__height):
                rectangle += "#" * self.__width + "\n"
        return rectangle[:-1]
