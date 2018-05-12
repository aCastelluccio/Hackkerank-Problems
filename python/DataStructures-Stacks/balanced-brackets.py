#!/bin/python3

import sys

def isBalanced(s):
    Stack = []
    yes = True
    for i in s:
        if i == '(' or i == '[' or i == '{':
            Stack.append(i)
        elif i == ')':
            if not Stack or Stack[-1] != '(':
                return "NO"
            Stack.pop()
        elif i == ']':
            if not Stack or Stack[-1] != '[':
                return "NO"
            Stack.pop()
        elif i == '}':
            if not Stack or Stack[-1] != '{' :
                return "NO"
            Stack.pop()
    if not Stack:
        return "YES"
    return "NO"
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
