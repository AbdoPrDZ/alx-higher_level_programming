#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print('0 arguments.')
    else:
        print('{0} arguments:'.format(argc - 1))
        for i in range(1, argc):
            print('{0}: {1}'.format(i, sys.argv[i]))
