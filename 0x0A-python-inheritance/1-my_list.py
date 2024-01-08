#!/usr/bin/python3
"""
1-my_list.py - Module defend an MyList class inherits from list
"""


class MyList(list):
    """
    MyList - inherits from list with print_sorted method
    """

    def print_sorted(self):
        """
        print_sorted - print this list in sorted form
        """

        print(sorted(self))
