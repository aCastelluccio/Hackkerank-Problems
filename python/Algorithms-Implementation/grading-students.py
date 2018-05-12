#!/bin/python3

import sys

def solve(grades):
    updated = []
    for i in grades:
        if(i > 37 ):
            if(i%5==0):
                updated.append(i)
            elif((i+1)%5==0):
                updated.append(i+1)
            elif((i+2)%5==0):
                updated.append(i+2)
            else:
                updated.append(i)
        else:
            updated.append(i)

    return updated
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
