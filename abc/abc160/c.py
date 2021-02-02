# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k,n = map(int,input().split())
a = list(map(int,input().split()))

ans = a[0] + (k - a[-1])
for i in range(n-1):
    ans = max(a[i+1] - a[i], ans)

print(k - ans)
