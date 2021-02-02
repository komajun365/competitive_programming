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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,*data = map(int,read().split())
xy = data[:2*(n-1)]
q = data[2*(n-1)]
ab = data[2*(n-1)+1:]

links = [[] for _ in range(n+1)]
it = iter(xy)
for x,y in zip(it,it):
    links[x].append(y)
    links[y].append(x)

root = 1
dbl = [[] for _ in range(n+1)]
dbl[root].append(root)
depth = [-1] * (n+1)
depth[root] = 0
stack = [root]
while(stack):
    i = stack.pop()
    for j in links[i]:
        if(depth[j] != -1):
            continue
        depth[j] = depth[i] + 1
        dbl[j].append(i)
        stack.append(j)

m = 20
for i in range(m-1):
    for j in range(1,n+1):
        up = dbl[j][i]
        dbl[j].append(dbl[up][i])

def calc(a,b):
    if(depth[a] < depth[b]):
        a,b = b,a
    dif = depth[a] - depth[b]
    a2,b2 = a,b
    for i in range(m):
        if(dif>>i)&1:
            a2 = dbl[a2][i]
    if(a2 == b2):
        return depth[a] - depth[b]
    
    for i in range(m-1,-1,-1):
        if(dbl[a2][i] != dbl[b2][i]):
            a2 = dbl[a2][i]
            b2 = dbl[b2][i]
    
    if(a2 != b2):
        a2 = dbl[a2][0]
        b2 = dbl[b2][0]
    
    res = (depth[a] - depth[a2]) + (depth[b] - depth[b2])
    return res

ans = []
it = iter(ab)
for a,b in zip(it,it):
    ans.append(calc(a,b) + 1)

print('\n'.join(map(str,ans)))







