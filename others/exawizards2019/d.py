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

n,x = map(int,input().split())
s = list(map(int,input().split()))
mod = 10**9 + 7

s.sort(reverse=True)
dp = [[0] * (10**5+1) for _ in range(n+1)]

dp[0][x] = 1
for i in range(n):
    for j in range(10**5+1):
        dp[i+1][j] += dp[i][j] * (n-1-i)
        dp[i+1][j%s[i]] += dp[i][j]
        dp[i+1][j] %= mod
        dp[i+1][j%s[i]] %= mod

ans = 0
for i in range(10**5+1):
    ans += i*dp[-1][i]
    ans %= mod

print(ans)


'''
Nmin(s)のオーダーでやれないか？

最終的にmにできる方法は？


min(si)で処理すれば値は確定する。
降順の順列だけ考えればいい。
これで2**N
大きい数字から処理したorしてないで場合分けして行けばいい？


'''
