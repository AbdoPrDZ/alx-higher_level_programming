#!/usr/bin/python3
import hidden_4
for item in dir(hidden_4):
    if not '__' in item:
        print(item)
