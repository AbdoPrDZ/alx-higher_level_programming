#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    raise_exception_msg - rase an exception with message

    Args:
        message (str, optional): the raise message. Defaults to "".

    Raise: NameError
    """

    print("{}".format(message), end="")

    raise NameError
