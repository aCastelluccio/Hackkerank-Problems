#!/bin/python3

import sys
import time
start_time = time.time()

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here

scores = list(set(scores))
scores.sort(reverse=True)
x = len(scores) - 1
for i in alice:
    while x >= 0 and i >= scores[x]:
            x -= 1
    print(x+2)
            
