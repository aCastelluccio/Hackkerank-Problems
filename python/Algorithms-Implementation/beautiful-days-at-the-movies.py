import sys
n,k,j = input().strip().split(' ')
n,k,j = [int(n),int(k),int(j)]
count=0
for x in range(n,k+1):
    bac = []
    for l in str(x):
        bac.append(l)
    back = ""
    for l in range(len(bac)):
        back+=bac[len(bac)-l-1]
    if (x-int(back))%j==0:
        count+=1
print(count)
