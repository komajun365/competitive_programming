# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n,k = map(int,readline().split())
data = [i.split() for i in readlines()]

cumsum_w = [[0] * (k+1) for _ in range(k+1)]
cumsum_b = [[0] * (k+1) for _ in range(k+1)]
for x,y,c in data:
    x = int(x)
    y = int(y)
    c = 0 if (c=='W') else 1
    c += x//k + y//k
    c %= 2
    x %= k
    y %= k
    if(c==0):
        cumsum_w[x][y] += 1
    else:
        cumsum_b[x][y] += 1

for i in range(k):
    for j in range(1,k):
        cumsum_w[i][j] += cumsum_w[i][j-1]
        cumsum_b[i][j] += cumsum_b[i][j-1]

for i in range(1,k):
    for j in range(k):
        cumsum_w[i][j] += cumsum_w[i-1][j]
        cumsum_b[i][j] += cumsum_b[i-1][j]

ans = 0
for x in range(k):
    for y in range(k):
        tmp = (cumsum_w[k-1][k-1]
                - cumsum_w[x-1][k-1]
                - cumsum_w[k-1][y-1]
                + 2 * cumsum_w[x-1][y-1]
                + cumsum_b[x-1][k-1]
                + cumsum_b[k-1][y-1]
                - 2 * cumsum_b[x-1][y-1])
        ans = max(ans,tmp)

        tmp = (cumsum_b[k-1][k-1]
                - cumsum_b[x-1][k-1]
                - cumsum_b[k-1][y-1]
                + 2 * cumsum_b[x-1][y-1]
                + cumsum_w[x-1][k-1]
                + cumsum_w[k-1][y-1]
                - 2 * cumsum_w[x-1][y-1])
        ans = max(ans,tmp)

print(ans)
