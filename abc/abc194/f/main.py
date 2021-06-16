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

n,k = input().split()
k = int(k)
mod = 10**9 + 7

dp = [[0] * 17 for _ in range(2)]
d = dict()
for i,ch in enumerate('0123456789ABCDEF'):
    d[ch] = i

head = n[0]
dp[0][1] = 1
dp[1][1] = d[head] - 1
dp[1][0] = 1

# print(dp)

use = [0] * 16
use[d[head]] = 1
for ch in n[1:]:
    num = d[ch]
    dp2 = [[0] * 17 for _ in range(2)]
    dp2[1][0] = 1
    used = sum(use[:num])
    nouse = num - used
    for i in range(1,17):
        if i == 1:
            dp2[1][i] = (dp[1][i] * i + dp[1][i-1] * 15
                            + dp[0][i] * used + dp[0][i-1] * nouse) % mod      
        else:
            dp2[1][i] = (dp[1][i] * i + dp[1][i-1] * (16-i+1)
                            + dp[0][i] * used + dp[0][i-1] * nouse) % mod
    use[num] = 1
    dp2[0][sum(use)] = 1

    dp,dp2 = dp2,dp
    # print(dp)
    # print(used,nouse)

ans = (dp[0][k] + dp[1][k]) % mod
print(ans)
 