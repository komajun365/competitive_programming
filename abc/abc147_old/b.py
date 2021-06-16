# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
n = len(s)
ans = 0
for i in range(n):
    j = n-1-i
    if(j <= i):
        break
    if(s[i] != s[j]):
        ans += 1

print(ans)
