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

n,x,*data = map(int,read().split())
h = data[:n]
ab = data[n:]
x -= 1

it = iter(ab)
links = [[] for _ in range(n)]
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

tp = []
parent = [-1] * n
parent[x] = -2
stack = [x]
while stack:
    i = stack.pop()
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        stack.append(j)
        tp.append(j)

tp = tp[::-1]

dp = h[::]
for i in tp:
    dp[parent[i]] = max(dp[parent[i]], dp[i])

print(max(0,sum(dp)*2-2))


