#!/usr/bin/python3
"""
This is the ``0-lookup`` task
"""


def lookup(obj):
    """
    Function that returns the list of available attributes and methods of an object
    """
    return dir(obj)
