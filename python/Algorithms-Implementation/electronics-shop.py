#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    keyboards.sort()
    drives.sort()
    biggest = 0
    for i in range(len(keyboards)-1,-1,-1):
        found = False
        x = len(drives) - 1
        while not found and x >= 0:
            if keyboards[i] + drives[x] <= s:
                if keyboards[i] + drives[x] > biggest:
                    biggest = keyboards[i] + drives[x]
                found = True
            x -= 1
    if biggest==0:
        return -1
    return biggest


s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
