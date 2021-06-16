# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
mod = 2019
remains = [0]*mod

ans = 0
now = 0
remains[0] = 1
for i,val in enumerate(s[::-1]):
    now += int(val) * pow(10,i,mod )
    now %= mod
    ans += remains[now]
    remains[now] += 1

print(ans)
