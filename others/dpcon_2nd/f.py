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

s = input()
t = input()

ls = len(s)
lt = len(t)

dp = [[0] * (ls+1) for _ in range(lt+1)]
for i,ti in enumerate(t,1):
    for j,sj in enumerate(s,1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        if(ti==sj):
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

ans = ''
i=lt
j=ls
while(i>0)&(j>0):
    if(dp[i][j] == dp[i][j-1]):
        j -= 1
    elif(dp[i][j] == dp[i-1][j]):
        i -= 1
    else:
        ans += s[j-1]
        i -= 1
        j -= 1

print(ans[::-1])
