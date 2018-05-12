#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here
biggest = 0
for i in height:
    if i >=k:
        rem = i - k
        if rem > biggest:
            biggest = rem
print(biggest)
    
