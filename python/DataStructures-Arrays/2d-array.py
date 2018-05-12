#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t= [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
sum = 0
max = -10000
a = 0
r = 0
for i in range(4):
    for a in range(4):
        sum += arr[a][r] + arr[a][r+1] + arr[a][r+2]
        sum += arr[a+2][r] + arr[a+2][r+1] + arr[a+2][r+2]
        sum += arr[a+1][r+1]
        if sum > max:
            max = sum
        sum = 0
    r+=1

print(max)
