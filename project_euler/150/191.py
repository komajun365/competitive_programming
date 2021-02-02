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

n = 4
dp = [[0] * 6 for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    dp[i+1][0] += dp[i][0] + dp[i][1] + dp[i][2]
    dp[i+1][1] += dp[i][0]
    dp[i+1][2] += dp[i][1]
    dp[i+1][3] += sum(dp[i])
    dp[i+1][4] += dp[i][3]
    dp[i+1][5] += dp[i][4]

print(sum(dp[-1]))

'''
dp[i][j][k] := i日目の時点でj回連続で休んでいて、k回遅刻した生徒

3次元めんどいので、
dp[i][j] := (j%3)回連続で休んでいて、(j//3)回遅刻した、とする
0<=j<=5

'''
