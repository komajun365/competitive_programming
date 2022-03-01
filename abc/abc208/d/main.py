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

n,m,*abc = map(int,read().split())

inf = 10**9
d = [[inf] * n for _ in range(n)]
it = iter(abc)
for a,b,c in zip(it,it,it):
    a -= 1
    b -= 1
    d[a][b] = c
for i in range(n):
    d[i][i] = 0

ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])
            if d[i][j] != inf:
                ans += d[i][j]
print(ans)
