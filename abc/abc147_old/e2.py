# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
b = [list(map(int,input().split())) for _ in range(h)]

for i in range(h):
    for j in range(w):
        a[i][j] = abs(a[i][j] - b[i][j])

base = 2**12800 - 1
dp = [[0] * (w+1) for _ in range(h+1)]
dp[1][1] = (2**6400 >> a[0][0])|(2**6400 << a[0][0])&base
for i in range(1,h+1):
    for j in range(1,w+1):
        if(i==1)&(j==1):
            dp[1][1] = (2**6400 >> a[0][0])|(2**6400 << a[0][0])&base
            continue

        dp[i][j] = ((dp[i-1][j] >> a[i-1][j-1])|(dp[i-1][j] << a[i-1][j-1])|
                    (dp[i][j-1] >> a[i-1][j-1])|(dp[i][j-1] << a[i-1][j-1]))&base

ans = 6400
ans_bit = dp[-1][-1]
for i in range(6300,6500):
    if((ans_bit >> i)&1 == 1):
        ans = min(ans, abs(6400-i))

print(ans)
