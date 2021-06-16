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

n,*ab = map(int,read().split())
links = [[] for _ in range(n)]

it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

def bfs(links, root):
    depth = [-1] * n
    depth[root] = 0
    stack = [root]
    while stack:
        stack2 = []
        for i in stack:
            for j in links[i]:
                if depth[j] != -1:
                    continue
                depth[j] = depth[i] + 1
                stack2.append(j)
        stack,stack2 = stack2,stack
    return i,depth

last,_ = bfs(links, 0)
last,depth = bfs(links, last)
print(depth[last] + 1)