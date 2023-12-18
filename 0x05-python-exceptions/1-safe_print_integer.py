#!/usr/bin/python3
def safe_print_integer(value):
    """ print an integer in sage way

    Args:
        value (int): the integer

    Return: True if value has been correctly printed
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
