# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7

cs = [0] * (n+1)
for i in range(n):
    cs[i+1] = cs[i] + a[i]

ans = 0
dp = [0] * (n+1)
dp[0] = 1
for i in range(1,n+1):
    dp2 = [0] * (n+1)
    cnt = [0] * i
    cnt[0] = dp[0]
    for j in range(1,n+1):
        k = cs[j] % i
        dp2[j] = cnt[k]
        cnt[k] += dp[j]
        cnt[k] %= mod
    dp,dp2 = dp2,dp
    ans += dp[-1]
    ans %= mod

print(ans)
