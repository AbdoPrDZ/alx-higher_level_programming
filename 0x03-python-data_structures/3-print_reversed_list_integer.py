#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer - Print list in reverse
    @my_list: The list want to print
    """
    mLen = len(my_list)
    for i in range(1, mLen + 1):
        print('{:d}'.format(my_list[-i]))
