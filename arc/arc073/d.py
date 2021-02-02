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

n,w = map(int,readline().split())
wv = list(map(int,read().split()))

inf = -1 * 10**10
dp = [[inf] * (301) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    wi,vi = wv[i*2:i*2+2]
    wi -= wv[0]
    for j in range(n,0,-1):
        for k in range(wi,301):
            dp[j][k] = max(dp[j][k], dp[j-1][k-wi] + vi)

ans = 0
for i in range(n+1):
    for j in range(301):
        if(i*wv[0] + j <= w):
            ans = max(ans,dp[i][j])

print(ans)


'''
dp[i][j][k] := i個目のものまで見て、jこ入ってて、追加がkの時の最大価値

dp[j][k]
にして、jを上から更新しましょう。
'''
