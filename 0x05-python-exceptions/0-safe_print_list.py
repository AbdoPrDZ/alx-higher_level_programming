#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    safe_print_list - print x of list elements

    Args:
        my_list (list, optional): the list. Defaults to [].
        x (int, optional): number of elements. Defaults to 0.

    Returns:
        int: number of printed elements
    """
    i = 0
    if my_list != None:
        try:
            for i in range(x):
                print('{}'.format(my_list[i]), end="")
        except IndexError:
            pass

        print("")

    return i
