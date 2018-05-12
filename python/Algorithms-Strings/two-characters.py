#!/bin/python3

import sys


s_len = int(input().strip())
s = input().strip()
abc = "abcdefghijklmnopqrstuvwxyz"
biggest = 0
for x in abc:
    for y in abc:
        list1= []
        for z in s:
            if z==x or z==y:
                list1.append(z)
        truth = True
        for w in range(len(list1)-2):
            if list1[w] != list1[w+2]:
                truth = False
        if(truth) and len(list1) > biggest and len(list(set(list1)))==2:

            biggest = len(list1)
print(biggest)
