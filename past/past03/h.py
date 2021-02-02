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

n,l = map(int,input().split())
x = list(map(int,input().split()))
t = list(map(int,input().split()))

hurdle = [0] * (l+1)
for i in x:
    hurdle[i] = 1

inf = 10**10
dp = [inf] * (l+1)
dp[0] = 0
for i in range(1,l+1):
    dp[i] = min(dp[i], dp[i-1] + t[0] + hurdle[i]*t[2])
    if(i >=2):
        dp[i] = min(dp[i], dp[i-2] + t[0] + t[1] + hurdle[i]*t[2])
    if(i >=4):
        dp[i] = min(dp[i], dp[i-4] + t[0] + t[1]*3 + hurdle[i]*t[2])

ans = dp[-1]
ans = min(ans,dp[-2] + (t[0] + t[1])//2)
if(l>=2):
    ans = min(ans,dp[-3] + (t[0] + t[1]*3)//2)
if(l>=3):
    ans = min(ans,dp[-4] + (t[0] + t[1]*5)//2)

print(ans)
