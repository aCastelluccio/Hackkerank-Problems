#!/bin/python3

import sys

def leftRotation(a, d):

    lent = len(a)
    a = a + a
    return a[d:d+lent]

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))
