#!/usr/bin/python3
def raise_exception_msg(message=""):
    """rase an exception with message

    Args:
        message (str, optional): the raise message. Defaults to "".

    Raise: Error
    """

    print("{}".format(message), end="")

    raise NameError
