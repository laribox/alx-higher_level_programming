#!/usr/bin/python3
"""
Task 3. Same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """Tells whether `obj` is an instance of `a_class` or any of its subclasses

    Args:
        obj: Object to check
        a_class: Class to check against

    Return:
        True if the object is an instance of any of them
        False if not
    """
    return isinstance(obj, a_class)
