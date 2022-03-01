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
p = list(map(int,input().split()))
q = list(map(int,input().split()))
mod = 998244353

r = [0] * n
for pi,qi in zip(p,q):
    r[pi-1] = qi-1

ans = 0
dp = [[0] * (n+1) for _ in range(n)]
for idx in range(n-1,-1,-1):
    i = r[idx]
    for idx2 in range(idx+1,n):
        right = r[idx2]
        if i > right:
            plus = 1
            for mid in range(idx+1,idx2):
                if r[mid] < right:
                    plus += 1
            for j in range(n-plus+1):
                dp[i][j+plus] += dp[right][j]
                dp[i][j+plus] %= mod
    dp[i][1] += 1
    dp[i][1] %= mod

    left = 0
    for idx2 in range(idx):
        if i > r[idx2]:
            left += 1
    if left < k:
        ans += dp[i][k-left]
        ans %= mod
    # print(ans,left)
    # print(dp[i])

print(ans)





