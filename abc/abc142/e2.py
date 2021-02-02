# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())

ab = []
c = []
for _ in range(m):
    ab_i = tuple(map(int,input().split()))
    ab.append(ab_i)
    c_i = tuple(map(int,input().split()))
    c_i_bit = 0
    for j in c_i:
        c_i_bit += 1 << (j-1)
    c.append(c_i_bit)

inf = 10**10
dp = [ [inf] * 2**n for _ in range(m+1) ]
dp[0][0] = 0

for i in range(m):
    for j in range(2**n):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][j|c[i]] = min(dp[i+1][j|c[i]], dp[i][j] + ab[i][0])

ans = dp[-1][-1]
if(ans == inf):
    print(-1)
else:
    print(ans)
