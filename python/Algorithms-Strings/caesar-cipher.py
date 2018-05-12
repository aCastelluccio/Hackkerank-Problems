#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())
alph = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alph2 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
ar = []
ar = alph.split()
ar2 = []
ar2 = alph2.split()
str = ""
for i in s:
    if i in ar:
        numToPrint = ar.index(i) + k
        while numToPrint > 25:
            numToPrint-=26
        str+=ar[numToPrint]
    elif i in ar2:
        numToPrint = ar2.index(i) + k
        while numToPrint > 25:
            numToPrint-=26
        str+=ar2[numToPrint]
    else:
        str+=i
print(str) 
