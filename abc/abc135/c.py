# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
for i in range(n-1, -1,-1):
    if(a[i+1] >= b[i]):
        ans += b[i]
        continue
    ans += a[i+1]
    b[i] -= a[i+1]
    tmp = min(a[i], b[i])
    ans += tmp
    a[i] -= tmp

print(ans)
