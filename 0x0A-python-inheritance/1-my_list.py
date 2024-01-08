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

        sl = []

        for n in self:
            for i in range(len(sl)):
                if n < sl[i]:
                    sl.insert(i, n)
                    break
            else:
                sl.append(n)

        print(sl)
