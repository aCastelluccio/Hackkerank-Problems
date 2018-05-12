#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
counta = 0
countb = 0
for i in apple:
    if(i + a >= s and i + a <= t):
        counta+=1
for i in orange:
    if(i + b >= s and i + b <= t):
        countb+=1
print(counta)
print(countb)
