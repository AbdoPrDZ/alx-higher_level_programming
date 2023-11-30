#!/usr/bin/python3
from string import ascii_uppercase
print(*map(lambda c: c, list(ascii_uppercase)), sep='')
