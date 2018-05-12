import sys


def kangaroo(x1, v1, x2, v2):
    if v1 < v2 and x1 < x2:
        return("NO")
    if v1 > v2 and x1 > x2:
        return("NO")
    start = x1
    start2 = x2
    for i in range(10000):
        start+=v1
        start2+=v2
        if start == start2:
            return("YES")
    return("NO")

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
