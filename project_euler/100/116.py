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

tn = 50
n = tn + 5
dp = [0] * (n+1)
dp[0] = 1

ans = 0
for j in [2,3,4]:
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(tn):
        dp[i+1] += dp[i]
        dp[i+j] += dp[i]
    ans += dp[tn]-1

print(ans)


'''
dpですよね？



'''
