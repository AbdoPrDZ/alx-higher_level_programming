#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    """
    safe_function - executes a function safely

    Args:
        fct (any): the pointer to a function

    Returns:
        any: the result of the function, None on error
    """
    try:
        return (fct(*args))
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
