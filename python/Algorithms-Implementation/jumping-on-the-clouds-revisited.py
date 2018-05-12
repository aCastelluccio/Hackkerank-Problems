#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
tot = 100
j = 0
for i in range(n):
    temp = (j + k) % n
    j = temp
    if c[temp] == 1:
        tot -=2
    tot -= 1

    if temp == 0:
        break
print (tot)
