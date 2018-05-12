#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a.sort()
biggest = 0
for i in range(len(a)):
    count = 0
    x = i
    while x < n and abs(a[i] - a[x]) <= 1:
        count+=1
        x+=1
    if count > biggest:
        biggest = count

print(biggest)
