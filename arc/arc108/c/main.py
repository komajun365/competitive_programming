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

n,m,*uvc = map(int,read().split())
links = [[] for _ in range(n+1)]
it = iter(uvc)
for u,v,c in zip(it,it,it):
    links[u].append([c,v])
    links[v].append([c,u])

root = 1
parent = [[-1,-1] for _ in range(n+1)]
parent[root] = [0,0]
stack = [root]
tp = []
while(stack):
    i = stack.pop()
    for c,j in links[i]:
        if(parent[j][1] != -1):
            continue
        parent[j] = [c,i]
        stack.append(j)
        tp.append(j)

num = [-1] * (n+1)
num[root] = 1
for i in tp:
    c,p = parent[i]
    if(num[p] == c):
        num[i] = c%n + 1
    else:
        num[i] = c

print('\n'.join(map(str,num[1:])))
