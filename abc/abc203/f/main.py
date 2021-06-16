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
a = list(map(int,input().split()))
a.sort()

left = [0] * (n+1)
l = 0
for r in range(n):
    while a[r]//2 >= a[l]:
        l += 1
    left[r] = l

dp = [[0] * (n+1) for _ in range(31)]
for j in range(n+1):
    dp[0][j] = j
for i in range(1,31):
    for j in range(1,n+1):
        dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][left[j-1]])

# for i in range(n):
#     print(dp[i])

for i in range(31):
    if dp[i][-1] <= k:
        print('{} {}'.format(i, dp[i][-1]))
        exit()

