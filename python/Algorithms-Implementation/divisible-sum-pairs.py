#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    tot = 0
    for i in range(len(ar)):

        for x in range(i+1,len(ar)):

            if (ar[i] + ar[x]) % k == 0:
                tot += 1

    return tot

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
