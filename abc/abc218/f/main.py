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

n,m,*st = map(int,read().split())
for i in range(m*2):
    st[i] -= 1

idx = dict()
links = [[] for _ in range(n)]
for i in range(m):
    s,t = st[i*2:i*2+2]
    links[s].append(t)
    idx[(s<<10) + t] = i

def solve(links, s,t):
    depth = [-1] * n
    parent = [-1] * n
    depth[0] = 0
    stack = [0]
    while stack:
        stack2 = []
        for i in stack:
            for j in links[i]:
                if [i,j] == [s,t] or depth[j] != -1:
                    continue
                depth[j] = depth[i] + 1
                parent[j] = i
                stack2.append(j)
        stack,stack2 = stack2,stack
    
    return depth,parent

dep,par = solve(links, -1,-1)

if dep[n-1] == -1:
    ans = [-1] * m
    print('\n'.join(map(str,ans)))
    exit()

# print(idx)
# print(dep)
# print(par)

ans = [dep[n-1]] * m
route = []
x = n-1
while x != 0:
    p = par[x]
    route.append(idx[(p<<10) + x])
    x = p

for x in route:
    s,t = st[x*2:x*2+2]
    dep, _ = solve(links,s,t)
    ans[x] = dep[n-1]

print('\n'.join(map(str,ans)))


