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
n2 = n*2+1

inf = 10**9
dp = [[inf] * (n2) for _ in range(n2)]
for i in range(n2):
    dp[i][i] = 0

for d in range(2,n2,2):
    for l in range(n2):
        r = l + d
        if r >= n2:
            break
        for m in range(l+1,r,2):
            dp[l][r] = min(dp[l][r], dp[l+1][m]+dp[m+1][r]+abs(a[l]-a[m]))
print(dp[0][-1])
