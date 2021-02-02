import sys
import os
f = open('C:\\Users\\scare\\Documents\\git\\atcoder\\input.txt', 'r')
sys.stdin = f

###############################################

n = int(input())
s = input()

ans = 1
for i in range(n-1):
    if s[i] != s[i+1]:
        ans += 1

print(ans)
