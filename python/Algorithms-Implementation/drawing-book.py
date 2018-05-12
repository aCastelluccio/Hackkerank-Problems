#!/bin/python3

import sys

def solve(n, p):
    if n==p:
        return 0
    if p > n//2:
        if n %2 == 0 and p%2!=0:
            return (n-p)//2+1
        return (n - p)//2
    else:
        return (p)//2

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
