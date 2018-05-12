#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    if (m + s - 1) % n != 0:
         return (m+s-1)%n
    else:
        return n
t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
