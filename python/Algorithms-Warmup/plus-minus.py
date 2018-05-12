#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
totPos = 0;
totNeg = 0;
totZero = 0;
count = 0;
for n in arr:
    if(n > 0):
        totPos += 1
    if(n == 0):
        totZero += 1
    if(n < 0):
        totNeg += 1
    count+=1
print(totPos / count)
print(totNeg / count)
print(totZero / count)
