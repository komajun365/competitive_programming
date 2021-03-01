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

s = input()
k = int(input())
l = len(s)

sr = s[::-1]

ans = 0
dp = [[0] * (l+1) for _ in range(l+1)]
for i in range(1,l+1):
    for j in range(1,l+1):
        if i+j > l+1:
            break
        if i+j == l+1:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            if s[i-1] == sr[j-1]:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+2)
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

ans = max( max(i) for i in dp)

for m in range(k):
    dp2 = [[0] * (l+1) for _ in range(l+1)]
    for i in range(1,l+1):
        for j in range(1,l+1):
            if i+j > l+1:
                break
            if i+j == l+1:
                dp2[i][j] = max(dp2[i-1][j-1] + 1, dp[i-1][j-1] + 1)

            else:
                if s[i-1] == sr[j-1]:
                    dp2[i][j] = max(dp2[i-1][j],dp2[i][j-1],dp2[i-1][j-1]+2,dp[i-1][j-1]+2)
                else:
                    dp2[i][j] = max(dp2[i-1][j],dp2[i][j-1],dp2[i-1][j-1],dp[i-1][j-1]+2)
    dp,dp2 = dp2,dp
            
    ans = max(ans, max( max(i) for i in dp))

print(ans)