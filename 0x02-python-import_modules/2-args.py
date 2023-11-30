#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print('{} arguments.'.format(0))
    else:
        if argc == 2:
            print('{} argument:'.format(1))
        else:
            print('{} arguments:'.format(argc - 1))
        for pos, item in enumerate(argv):
            if not (pos == 0):
                print('{0}: {1}'.format(pos, item))
