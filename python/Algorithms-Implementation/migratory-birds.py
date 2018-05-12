#!/bin/python3

import sys

def migratoryBirds(n, ar):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    for i in ar:
        if i == 1:
            one+=1
        if i == 2:
            two+=1
        if i == 3:
            three+=1
        if i == 4:
            four+=1
        if i == 5:
            five+=1
    if one >= max(two,three,four,five):
        return 1;
    if two >= max(one,three,four,five):
        return 2;
    if three >= max(two,one,four,five):
        return 3;
    if four >= max(two,three,one,five):
        return 4;
    if five >= max(two,three,four,one):
        return 5;
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
