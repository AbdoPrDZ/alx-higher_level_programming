#!/usr/bin/python3
if __name__ == '__main__':
    """
    Program to calculate a with b
    """
    from sys import argv
    from calculator_1 import add, sub, mul, div

    OPERATIONS = ['+', '-', '*', '/']

    argc = len(argv)
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    op = argv[2]
    if not (op in OPERATIONS):
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    fu = add if op == '+' else sub if op == '-' else mul if op == '*' else div

    print('{0} {1} {2} = {3}'.format(a, op, b, fu(a, b)))
