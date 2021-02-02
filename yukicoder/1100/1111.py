# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,k = map(int,readline().split())
pqc = list(map(int,read().split()))
mod = 10**9+7

links = [dict() for _ in range(300+1)]
it = iter(pqc)
for p,q,c in zip(it,it,it):
    links[p][q] = c

dp = [0,0]
dp[0] = [[0] * (k+1) for _ in range(300+1)]
dp[1] = [[0] * (k+1) for _ in range(300+1)]
for j in range(1,300+1):
    dp[0][j][0] = 1

for i in range(n-1):
    i %= 2
    i_next = 1-i
    dp[i_next] = [[0] * (k+1) for _ in range(300+1)]
    for j in range(1,301):
        for key,val in links[j].items():
            for l in range(k-val+1):
                dp[i_next][j][l+val] += dp[i][key][l]
                dp[i_next][j][l+val] %= mod

ans = 0
for j in range(1,301):
    ans += dp[i_next][j][k]

ans %= mod
print(ans)



'''



'''
