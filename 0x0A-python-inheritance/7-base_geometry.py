#!/usr/bin/python3
"""Task 6. Improve Geometry"""


class BaseGeometry():
    """empty class """
    def area(self):
        """raises an exception if method not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Public instance method that validates `value`

        Args:
            name (string): Name
            value: Value of `name`

        Raises:
            TypeError if `value` is not an integer
            ValueError if `value` is <= zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
