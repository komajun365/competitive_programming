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

n,uv = map(int,read().split())
mod = 10**9 + 7

links = [[] for _ in range(n)]
it = iter(uv)
for u,v in zip(it,it):
    u -= 1
    v -= 1
    links[u].append(v)
    links[v].append(u)

root = 0
parent = [-1] * n
parent[root] = -2
tp = []
stack = [root]
while stack:
    i = stack.pop()
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        tp.append(j)
        stack.append(j)

tp = tp[::-1]

dp0 = [[0] * (n+1) for _ in range(n)] # 子に警備員がいる
dp1 = [[0] * (n+1) for _ in range(n)] # 子に警備員がいない
