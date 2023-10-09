#!/usr/bin/python3
"""task 8. Rectangle"""


class BaseGeometry:
    """BaseGeometry class with methods"""
    def area(self):
        """raises an exception if method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates `value`

        Args:
            name (str): Name
            value: Value of `nam`

        Raises:
            TypeError if `value` is not an integer
            ValueError if `value` is <= zero
        """
        
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """a Rectangle class which inherits BaseGeometry"""
    def __init__(self, width, height):
        """instatiates the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
