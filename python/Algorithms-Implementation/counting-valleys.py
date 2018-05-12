#!/bin/python3

import sys
steps = input()
m = input().strip().split(' ')
n = m[0]
up = 0
valley = 0

for i in range(len(n)-1):
    if n[i]==("U"):
        up+=1
    if n[i]==("D"):
        if up == 0:
            valley+=1
        up-=1
print(valley)
