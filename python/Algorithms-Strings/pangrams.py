
import sys

s = input().strip().lower()
count = 0
comp = "abcdefghijklmnopqrstuvwxyz"
s_ar = list(s)
ar = list(comp)

if len(set(s_ar).intersection(ar)) == len(ar):
    print("pangram")
else:
    print("not pangram")
