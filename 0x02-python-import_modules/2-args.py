#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    print('{} '.format(len(argv) - 1), end='')
    if len(argv) == 1:
        print('arguments.')
    elif len(argv) == 2:
        print('argument:')
    else:
        print('arguments:')
    for i in range(1, len(argv)):
        print('{0}: {1}'.format(i, argv[i]))
