#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
tot = 0
for i in arr:
    tot = tot + i
print(tot)
