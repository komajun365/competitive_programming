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

l,r = map(int,input().split())
mod = 10**9 + 7
n = r.bit_length()

dp = [[0] * (4) for _ in range(n+1)]

for i in range(n):
    m = n-i-1
    if(2**(m+1) <= l):
        break

    ri = (r >> m)&1
    li = (l >> m)&1

    if(i==0):
        if(li==0):
            dp[i+1][2] += 1
        else:
            dp[i+1][0] += 1
    else:
        if(li==0):
            dp[i+1][3] += 1
        else:
            dp[i+1][1] += 1


for i in range(n):
    m = n-i-1
    ri = (r >> m)&1
    li = (l >> m)&1

    if(ri==li==0):
        dp[i+1][0] += dp[i][0]
        dp[i+1][1] += dp[i][1] * 2
        dp[i+1][2] += dp[i][2]
        dp[i+1][3] += dp[i][1] + dp[i][3]*3
    elif(ri==0) and (li==1):
        dp[i+1][1] += dp[i][1]
        dp[i+1][2] += dp[i][2]
        dp[i+1][3] += dp[i][3]*3
    elif(ri==1) and (li==0):
        dp[i+1][0] += dp[i][0]
        dp[i+1][1] += dp[i][0] + dp[i][1] * 2
        dp[i+1][2] += dp[i][0] + dp[i][2] * 2
        dp[i+1][3] += dp[i][1] + dp[i][2] + dp[i][3]*3
    else:
        dp[i+1][0] += dp[i][0]
        dp[i+1][1] += dp[i][1]
        dp[i+1][2] += dp[i][2] * 2
        dp[i+1][3] += dp[i][2] + dp[i][3]*3
    dp[i+1][0] %= mod
    dp[i+1][1] %= mod
    dp[i+1][2] %= mod
    dp[i+1][3] %= mod

ans = sum(dp[-1]) % mod
print(ans)

# print(dp)
