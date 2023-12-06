#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    search_replace - replaces all occurrences of an element
                     by another in a new list
    @my_list: is the initial list
    @search: is the element to replace in the list
    @replace: is the new element
    """
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])

    return new_list
