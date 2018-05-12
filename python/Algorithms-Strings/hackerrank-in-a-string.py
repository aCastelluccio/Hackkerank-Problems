
import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    count = 0
    comp = "hackerrank"
    for i in s:
        if count < len(comp) and i == comp[count]:
            count += 1
    if count == len(comp):
        print("YES")
    else:
        print("NO")
