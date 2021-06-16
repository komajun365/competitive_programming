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



n,k = map(int,input().split())
mod = 10**9 + 7

max_n = n + 10
fac, finv, inv = [0]*max_n, [0]*max_n, [0]*max_n

# head
dp = [0] * n
dp[0] = 1
for i in range(k-1):
    dp2 = [0] * (n-i)
    dp2[0] = dp[0]
    for j in range(n-1-i):
        dp2[j] += dp2[j-1] + dp[j+1]
        dp2[j] %= mod
    dp,dp2 = dp2,dp

ans = sum(dp) % mod
ans *= pow(2, max(0,n-k-1), mod)
ans %= mod
print(ans)



"""
dp[i][j] := i個処理済みでlとrの間にj個数がある
dp[i+1][j] = dp[i][0~(j)] + dp[i][j+1]

(4 3 2)
243
342
324
432
423

(5 4 3 2)
2543
3542
3524



"""
