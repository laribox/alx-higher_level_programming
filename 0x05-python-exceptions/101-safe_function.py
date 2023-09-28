#!/usr/bin/python3
"""function that executes a function safely."""
def safe_function(fct, *args):
    try:
        r = fct(*args)
        return r
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
