#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

ar = []
ar2 = []
ar3 = []
ar.append(h1.pop())
ar2.append(h2.pop())
ar3.append(h3.pop())
for i in range(len(h1)):
    ar.append(h1.pop() + ar[-1])
for i in range(len(h2)):
    ar2.append(h2.pop() + ar2[-1])
for i in range(len(h3)):
    ar3.append(h3.pop() + ar3[-1])

tmp = set(ar).intersection(ar2)
tmp = tmp.intersection(ar3)
if not tmp:
    print (0)
else:
    print(max(tmp))
