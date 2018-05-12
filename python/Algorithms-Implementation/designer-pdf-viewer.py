#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
biggest = 0
for i in word:
    j = 0
    while alphabet[j] != i:
        j += 1
    if h[j] > biggest:
        biggest = h[j]
print(biggest * len(word))
            
