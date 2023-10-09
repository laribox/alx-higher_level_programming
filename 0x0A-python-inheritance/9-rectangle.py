#!/usr/bin/python3
"""Task 9-rectangle"""
parentClass = __import__("7-base_geometry").BaseGeometry


class Rectangle(parentClass):
    """Inherits baseG and initializes a Rectangle"""

    def __init__(self, width, height):
        """Initializes instance of `BaseGeometry`"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height
