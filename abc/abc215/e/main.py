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
s = input()
mod = 998244353

dp = [[0] * 1024 for _ in range(10)]

for i in range(n):
    dp2 = [[0] * 1024 for _ in range(10)]
    x = ord(s[i]) - ord('A')
    dp2[x][1<<x] = 1
    for j in range(10):
        for k in range(1024):
            if dp[j][k] == 0:
                continue
            
            dp2[j][k] += dp[j][k]
            dp2[j][k] %= mod
            if j == x:
                dp2[j][k] += dp[j][k]
                dp2[j][k] %= mod
            else:
                if (k >> x) & 1:
                    pass
                else:
                    dp2[x][k + (1<<x)] += dp[j][k]
                    dp2[x][k + (1<<x)] %= mod
    dp,dp2 = dp2,dp

ans = 0
for i in range(10):
    ans += sum(dp[i]) % mod

ans %= mod
print(ans)




