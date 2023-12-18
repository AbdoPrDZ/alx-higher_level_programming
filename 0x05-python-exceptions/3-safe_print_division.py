#!/usr/bin/python3
def safe_print_division(a, b):
    """ print the division result of a and b in sage way

    Args:
        a (int): the first number
        b (int): the second number

    Return: the result of division or None on fail
    """
    rd = None
    
    try:
        rd = a / b
    except:
        pass
    finally:
        print('Inside result: {}'.format(rd))

    return rd
