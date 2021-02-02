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
mod = 998244353

dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = 1

for x in range(-n,n+1):
    ini = max(0,x)
    tot = 0
    for i in range(ini,n+1):
        j = i-x
        if(j > n):
            break
        tot += dp[i][j]
        tot %= mod
        if(j%2==0) and (j!=0):
            dp[i][j//2] += tot
            dp[i][j//2] %= mod

ans = 0
for i in range(k+1):
    if(n-i < 0):
        break
    ans += dp[n-i][k-i]
    ans %= mod

print(ans)
# if(n == 4):
#     print(dp)