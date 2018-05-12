#!/bin/python3

import sys

def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    i = 0
    while i < len(ar)-1:
        if ar[i] == ar[i+1]:
            pairs+=1
            i+=2
        else:
            i+=1
    return pairs


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
