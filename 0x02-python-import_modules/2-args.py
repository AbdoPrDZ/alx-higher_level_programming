#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    argc = len(argv)

    print('{} '.format(argc - 1), end='')
    if argc == 1:
        print('arguments.')
    elif argc == 2:
        print('argument:')
    else:
        print('arguments:')

    for i in range(1, argc):
        print('{0}: {1}'.format(i, argv[i]))
