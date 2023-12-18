#!/usr/bin/python3
def safe_print_division(a, b):
    """
    safe_print_division - print the division result of a and b in sage way

    Args:
        a (int): the first number
        b (int): the second number

    Return:
        int|None: the result of division or None on fail
    """
    rd = None

    try:
        rd = a / b
    except Exception:
        pass
    finally:
        print('Inside result: {}'.format(rd))

    return rd
