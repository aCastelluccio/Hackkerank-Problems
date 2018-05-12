#!/bin/python3

import sys


s = input().strip()
upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
count = 0
for x in s:
    if x in upper:
        count+=1
print(count+1)
