# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
s,t = input().split()
ans = ''
for i in range(n):
    ans += s[i] + t[i]
print(ans)
