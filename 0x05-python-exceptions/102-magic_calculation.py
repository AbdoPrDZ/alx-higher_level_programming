#!/usr/bin/python3
def magic_calculation(a, b):
    """
    magic_calculation - magic calculation of a and b

    Args:
        a (int|float): the first number
        b (int|float): the second number

    Raises:
        Exception: Too Far

    Returns:
        int|float: the calculation result
    """
    r = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                r += (a ** b) / i
        except:
            r = b + a
            break
    return r
