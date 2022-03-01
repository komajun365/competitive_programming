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
sys.setrecursionlimit(10**6)

n,*ab = map(int,read().split())
links = [[] for _ in range(n)]

it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

parent = [-1] * n
parent[0] = -2
size = [-1] * n
def bfs(x):
    sx = 1
    for i in links[x]:
        if i == parent[x]:
            continue
        parent[i] = x
        sx += bfs(i)
    size[x] = sx
    return size[x]

bfs(0)

route = [n-1]
while route[-1] != 0:
    x = route[-1]
    route.append(parent[x])

route = route[::-1]
l = len(route)
x = route[(l+1)//2]

if size[x] *2 >= n:
    print('Snuke')
else:
    print('Fennec')