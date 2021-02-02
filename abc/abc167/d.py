# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
a = list(map(int,input().split()))

dbl_max = (len(str(bin(k-1)))) -2
dbl = [[-1] * (n) for _ in range(dbl_max) ]

for j in range(n):
    dbl[0][j] = a[j] -1

for i in range(1,dbl_max):
    for j in range(n):
        dbl[i][j] = dbl[i-1][ dbl[i-1][j] ]

ans = 0
for i in range(dbl_max):
    if( (k >> i) & 1):
        ans = dbl[i][ans]

print(ans+1)
