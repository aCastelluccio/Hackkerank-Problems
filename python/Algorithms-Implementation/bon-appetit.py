#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    tot = 0
    for i in range(len(ar)):
        if i != k:
            tot += ar[i]
    tot = tot//2
    if tot == b:
        return "Bon Appetit"
    return int(b - tot)


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
