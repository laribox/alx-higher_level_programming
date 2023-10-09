#!/usr/bin/python3
"""Task 4. Only sub class of """


def inherits_from(obj, a_class):
    """return True if obj is an instance of subclass or class"""
    return isinstance(obj, a_class) and not obj.__class__ == a_class
