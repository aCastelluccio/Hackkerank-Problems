#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    i =  s[8:]
    num = int(s[0:2])
    if i == "PM" and num ==12:
        return s[:8]
    if i == "PM":
        num +=12
        return str(num)+s[2:8]
    if i == "AM" and num ==12:
        s = "00"+s[2:8]
        return s
    else:
        return s[:8]

s = input().strip()
result = timeConversion(s)
print(result)
