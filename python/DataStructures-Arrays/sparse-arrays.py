i = eval(input())
ar = []
for x in range(i):
    ar.append(input())
i2 = eval(input())
ar2 = []
for x in range(i2):
    ar2.append(input())
for k in ar2:
    tot = 0
    for j in range(i):
        if k == ar[j]:
            tot +=1
    print(tot)
