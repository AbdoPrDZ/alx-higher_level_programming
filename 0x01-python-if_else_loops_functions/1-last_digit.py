#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = abs(number) % 10 * (-1 if number < 0 else 1)
print(f'Last digit of {number} is {dig} and is ', end='')
if dig > 5:
    print("greater than 5")
elif dig == 0:
    print(0)
else:
    print("less than 6 and not 0")
