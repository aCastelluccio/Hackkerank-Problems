#!/bin/python3

import sys

def solve(n, s, d, m):
    tot = 0
    for x in range(len(s)):
        ps =  x
        sum = 0
        for i in range(m):
            if ps < len(s):
                sum = s[ps] + sum
                ps+=1

        if sum == d:
            tot+=1
    return tot

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
