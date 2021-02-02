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

n,m,*a = read().split()
n = int(n)
m = int(m)

ad = [[] for _ in range(11)]
for i in range(n):
    for j in range(m):
        x = a[i][j]
        if(x=='S'):
            ad[0].append([i,j])
        elif(x=='G'):
            ad[10].append([i,j])
        else:
            ad[int(x)].append([i,j])

inf = 10**9
dp = [[inf] * m for _ in range(n)]

i,j = ad[0][0]
dp[i][j] = 0
for k in range(10):
    for ai,aj in ad[k]:
        for bi,bj in ad[k+1]:
            dp[bi][bj] = min(dp[bi][bj], dp[ai][aj] + abs(ai-bi) + abs(aj-bj))

i,j = ad[10][0]
if(dp[i][j] >= inf):
    print(-1)
else:
    print(dp[i][j])

# print(ad)
# print(dp)