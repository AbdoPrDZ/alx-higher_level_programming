#!/usr/bin/python3
if __name__ == '__main__':
    """
    Print All names defended in hidden_4
    """
    import hidden_4

    for item in dir(hidden_4):
        if item[:2] == '__':
            print(item)
