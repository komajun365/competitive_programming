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

n,*data = map(int,read().split())

imos = [[0] * 1001 for _ in range(1001)]
it = iter(data)
for lx,ly,rx,ry in zip(it,it,it,it):
    imos[lx][ly] += 1
    imos[rx][ly] -= 1
    imos[lx][ry] -= 1
    imos[rx][ry] += 1

for i in range(1,1000):
    for j in range(1000):
        imos[i][j] += imos[i-1][j]

for i in range(1000):
    for j in range(1,1000):
        imos[i][j] += imos[i][j-1]

ans = [0] * (n+1)
for i in range(1000):
    for j in range(1000):
        ans[imos[i][j]] += 1
print('\n'.join(map(str,ans[1:])))