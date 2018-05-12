#!/bin/python3

import sys

def getTotalX(a, b):
    count = 0
    maxi = max(a)
    if(max(a)<max(b)):
        maxi = max(b)
    for i in range(1,100000):
            truth = True
            for x in a:
                if i%x!=0:
                    truth = False
            for x in b:
                if x%i!=0:
                    truth = False
            if truth:
                count+=1
    return count
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)
