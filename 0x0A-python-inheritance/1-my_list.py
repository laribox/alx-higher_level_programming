#!/usr/bin/python3
"""Inherits a list and prints it sorted"""


class MyList(list):
    """initializes the class"""
    def __init__(self):
        """inherit the list class init"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
