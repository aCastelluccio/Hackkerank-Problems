#!/bin/python3

import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    h = 1
    for x in range(n):
        if x % 2 == 0:
            h = h *2
        else:
            h = h + 1
    print(h)
