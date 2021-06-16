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

n,*data = read().split()
n = int(n)
c = data.pop()
xy = [int(i)-1 for i in data]

if n == 1:
    if c == 'B':
        print(0)
    else:
        print(1)
    exit()

deg = [0] * n
links = [set() for _ in range(n)]
it = iter(xy)
for x,y in zip(it,it):
    links[x].add(y)
    links[y].add(x)
    deg[x] += 1
    deg[y] += 1

color = [0] * n
for i,ci in enumerate(c):
    color[i] = 1 * (ci=='W')

leaf = []
for i in range(n):
    if deg[i] == 1:
        leaf.append(i)

use = [1] * n
while leaf:
    i = leaf.pop()
    if color[i] == 0:
        use[i] = 0
        deg[i] -= 1
        for j in links[i]:
            links[j].remove(i)
            deg[j] -= 1
            if deg[j] == 1:
                leaf.append(j)

n2 = sum(use)
if n2 <= 1:
    print(n2)
    exit()

for i in range(n):
    if use[i] == 0:
        color[i] = 0
    else:
        color[i] = (color[i] + deg[i]) % 2

for root in range(n):
    if use[root] == 1:
        break

stack = [root]
parent = [-1] * n
parent[root] = -2
tp = [root]
while stack:
    i = stack.pop()
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        stack.append(j)
        tp.append(j)

tp = tp[::-1]
dp = [[0,0] for _ in range(n)]

max_w = 0
for i in tp:
    dp[i].sort(reverse=True)
    if color[i] == 1:
        dp[i][0] += 1
    max_w = max(max_w, sum(dp[i][:2]))
    if i != root:
        p = parent[i]
        dp[p].append(dp[i][0])

ans = (n2-1)*2 + sum(color) - max_w*2
print(ans)
print(n2,max_w)
print(dp)




