#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    argc = len(argv)
    s = 0

    for i in range(1, argc):
        n = int(argv[i])
        s += n

    print('{}'.format(s))
