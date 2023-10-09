#!/usr/bin/python3
"""Task 6. Improve Geometry"""


class BaseGeometry():
    """empty class """
    def area(self):
        """raises an exception if method not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
