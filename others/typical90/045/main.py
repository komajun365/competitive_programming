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
read = sys.stdin.buffer.read

n,k,*data = map(int,read().split())
it = iter(data)
xy = [[x,y] for x,y in zip(it,it)]
# print(xy)

dij = [[0] * n for _ in range(n)]
d = [0] * (2**n)

for i in range(n):
    for j in range(n):
        dij[i][j] = (xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2

for i in range(n):
    bi = 2**i
    for j in range(1,2**i):
        d[bi+j] = d[j]
        for l in range(i):
            if (j>>l)&1 == 1:
                d[bi + j] = max(d[bi + j], dij[i][l])

inf = 10**20
dp = d[::]
# print(dp)
for i in range(k-1):
    dp2 = [inf] * (2**n)
    for j in range(1,2**n):
        x = j
        while x > j//2:
            x = (x-1) & j
            dp2[j] = min(dp2[j], max(dp[x],d[j-x]))
            
    dp,dp2 = dp2,dp
    # print(dp)
print(dp[-1])



