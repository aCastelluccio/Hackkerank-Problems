#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    Alice = 0
    Bob = 0
    if a0 > b0:
        Alice += 1
    elif a0 < b0:
        Bob += 1
    if a1 > b1:
        Alice += 1
    elif a1 < b1:
        Bob += 1
    if a2 > b2:
        Alice += 1
    elif a2 < b2:
        Bob += 1
    result = str(Alice) + " " + str(Bob)
    return result

a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(result)
