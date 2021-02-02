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

n = int(input())
mod = 10**9+7

dp = [0] * n
dp[0] = 1
tot = 1
for i in range(1,n):
    if(i==1):
        dp[i] = tot
    else:
        dp[i] = tot - dp[i-2]
    dp[i] %= mod
    tot += dp[i]
    tot %= mod

ans = 0
for i in range(n-1):
    ans += dp[i] * ((n-1)**2 + min(n-1, i+2))
    ans %= mod

ans += dp[-1]*n
ans %= mod
print(ans)

# print(dp)


'''
1以外が2個以上続いたらもう固定？

1
x,1*x (x+1個のセット)

dp[i] := i個目まで決まっていて、i+1個目を自由に決められる場合の数

dp[i] = sum(dp[j]) - dp[i-2] (0<= j < i-2)

1,1,1,2,4,7,12,...



'''
