#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    safe_print_list_integers - print x elements of list of integers in safely

    Args:
        my_list (list, optional): the list. Defaults to [].
        x (int, optional): the number of elements. Defaults to 0.

    Return:
        int: the number of printed elements
    """
    n = 0
    for i in range(x):
        el = my_list[i]
        try:
            print("{:d}".format(el), end="")
            n += 1
        except Exception:
            pass
    print("")

    return n
