#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer - Print list in reverse
    @my_list: The list want to print
    """
    if my_list:
        mLen = len(my_list)
        if mLen > 0:
            for i in range(mLen):
                print('{:d}'.format(my_list[-(i + 1)]))
