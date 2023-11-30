#!/usr/bin/python3
if __name__ == '__main__':
    """
    Program to calculate a with b
    """
    from sys import argv
    from calculator_1 import add, sub, mul, div

    OPERATIONS = ['+', '-', '*', '/']

    argc = len(argv)

    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    op = argv[2]
    if not (op in OPERATIONS):
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(argv[1])
    b = int(argv[2])
    s = 0

    if op == '+':
        s = a + b
    elif op == '-':
        s = a - b
    elif op == '*':
        s = a * b
    else:
        s = a / b

    print('{0} {1} = {2}'.format(a, op, b))
