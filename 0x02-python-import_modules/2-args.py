#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    aLen = len(argv)
    if aLen == 1:
        print('{} arguments.'.format(aLen - 1))
    else:
        if aLen == 2:
            print('{} argument:'.format(aLen - 1))
        else:
            print('{} arguments:'.format(aLen - 1))
        for i in range(1, aLen):
            print('{0}: {1}'.format(i, argv[i]))
