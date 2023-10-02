#!/usr/bin/python3
"""
code for Rectangle class with static function
"""


class Rectangle:
    """private attributes width and height"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """instanciates the class"""
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

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
        """returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
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
                rectangle += str(self.print_symbol) * self.__width + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """returns an instance of class Rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    @classmethod
    def __del__(cls):
        """prints a statement when the instance is deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
