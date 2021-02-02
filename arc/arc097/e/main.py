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

import sys
read = sys.stdin.read

n,*ca = read().split()
n = int(n)
w_ind = [-1] * n
b_ind = [-1] * n

for i in range(2*n):
    c,a = ca[i*2:i*2+2]
    a = int(a) - 1
    if(c == 'W'):
        w_ind[a] = i
    else:
        b_ind[a] = i

left_w = [[0] * (n+1) for _ in range(2*n+1)]
left_b = [[0] * (n+1) for _ in range(2*n+1)]
for left,ind in zip([left_w, left_b], [w_ind, b_ind]):
    for i,xi in enumerate(ind):
        left[xi+1][i] += 1
    for i in range(2*n+1):
        for j in range(n-1):
            left[i][j+1] += left[i][j]
    for i in range(2*n):
        for j in range(n):
            left[i+1][j] += left[i][j]

inf = 10**9
dp = [[inf] * (n+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(n+1):
        if i == n and j == n:
            continue
        elif i == n:
            dp[i][j+1] = min(dp[i][j+1],
                             dp[i][j] + b_ind[j] - left_w[b_ind[j]][i-1] - left_b[b_ind[j]][j-1])
        elif j == n:
            dp[i+1][j] = min(dp[i+1][j],
                             dp[i][j] + w_ind[i] - left_w[w_ind[i]][i-1] - left_b[w_ind[i]][j-1])
        else:
            dp[i][j+1] = min(dp[i][j+1],
                             dp[i][j] + b_ind[j] - left_w[b_ind[j]][i-1] - left_b[b_ind[j]][j-1])
            dp[i+1][j] = min(dp[i+1][j],
                             dp[i][j] + w_ind[i] - left_w[w_ind[i]][i-1] - left_b[w_ind[i]][j-1])

print(dp[-1][-1])