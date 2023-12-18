#!/usr/bin/python3
def safe_print_integer(value):
    """
    safe_print_integer - print an integer in sage way

    Args:
        value (int): the integer

    Return:
        bool: True if value has been correctly printed
    """
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
