#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
big = 0
small = arr[0]
tot = 0
tot2 = 0
cantbeTrue = False
for i in arr:
    if i > big:
        big = i
for i in arr:
    if i < small:
        small = i
for i in arr:
    if big != i or cantbeTrue:
        tot = tot + i
    if big == i:
        cantbeTrue = True
cantbeTrue = False
for i in arr:
    if small != i or cantbeTrue:
        tot2 = tot2 + i
    if small == i:
        cantbeTrue = True
print(tot,tot2)
