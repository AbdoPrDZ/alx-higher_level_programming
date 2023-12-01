#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    add_tuple - Calculate addition of two tuples
    @tuple_a: First tuple
    @tuple_b: Second tuple
    Return: Calculated tuple
    """

    aLen = len(tuple_a)
    bLen = len(tuple_b)

    a1 = tuple_a[0] if aLen >= 1 else 0
    a2 = tuple_a[1] if aLen > 1 else 0
    b1 = tuple_b[0] if bLen >= 1 else 0
    b2 = tuple_b[1] if bLen > 1 else 0

    return (a1 + b1, a2 + b2)
