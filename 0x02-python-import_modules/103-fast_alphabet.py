#!/usr/bin/python3
def put(i): return chr(i)
print(*map(put, range(65, 91)), sep='')
