#!/bin/python3

import sys

def super_reduced_string(s):
    str = ""
    ind = 0
    while len(s) > 0 and ind < len(s)-1:
        if s[ind] == s[ind+1]:
            s = s[:ind] + s[ind+2:]
            ind = 0
        else:
            ind+=1
    if len(s) > 0:
        return s
    return "Empty String"

s = input().strip()
result = super_reduced_string(s)
print(result)
