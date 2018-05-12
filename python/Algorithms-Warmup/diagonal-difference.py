#!/bin/python3

import sys
import math

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
tot = 0
tot2 = 0
count = 0
for j in range(n):
    tot = tot + a[j][j]
for j in range(n):
    tot = tot - a[j][-1*(j+1)]
if(tot<0):
    tot *= -1
print(tot)
