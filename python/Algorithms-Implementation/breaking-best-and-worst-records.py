#!/bin/python3

import sys

def getRecord(s):
    biggest = s[0]
    bigCount = 0
    lowest  =s[0]
    lowCount = 0
    for i in s:
        if i > biggest:
            bigCount+=1
            biggest = i
        if i < lowest:
            lowest = i
            lowCount+=1
    return [bigCount,lowCount]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
