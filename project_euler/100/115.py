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
f = open('p107_network.txt', 'r')
sys.stdin = f

n = 1000
m = 50
dp = [[0,0] for _ in range(n+1)]
dp[0][0] = 1

for i in range(1,n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    if(i >= m):
        dp[i][1] = dp[i-1][1] + dp[i-m][0]

    if( sum(dp[i]) > 10**6):
        print(i)
        break




'''
dpですよね？
dp[i][0] := i個まで敷き詰めた最後は黒
dp[i][1] := i個まで敷き詰めた最後は赤

m=3のとき
dp[j][0] = dp[j-1][0] + dp[j-1][1]
dp[j][1] = dp[j-3][0] + dp[j-4][0] + ... = dp[j-1][1] + dp[j-3][0]

'''
