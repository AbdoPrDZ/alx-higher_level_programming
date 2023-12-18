#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """
    safe_print_integer_err - prints an integer

    Args:
        value (any): the number

    Returns:
        bool: True if value has been correctly printed, False
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
