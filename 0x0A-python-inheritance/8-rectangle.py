#!/usr/bin/python3
"""task 8. Rectangle"""


parentClass = __import__("7-base_geometry").BaseGeometry


class Rectangle(parentClass):
    """a Rectangle class which inherits BaseGeometry"""
    def __init__(self, width, height):
        """instatiates the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
