#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ divides element by element 2 lists.

    Args:
        my_list_1 (list<int>): the first list
        my_list_2 (list<int>): the second list
        list_length (int): the length of two lists
    """
    result_list = []

    for i in range(list_length):
        dr = 0
        try:
            dr = my_list_1[i] / my_list_2[i]
        except (IndexError):
            print("out of range")
        except (ZeroDivisionError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        finally:
            result_list.append(dr)

    return result_list
