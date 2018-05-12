#!/bin/python3

import sys

biggest = 0
biggest_count = 1
n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
for i in height:
    if i >= biggest:
        if i == biggest:
            biggest_count += 1
        else:
            biggest = i
print(biggest_count)    
