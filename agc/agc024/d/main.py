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
deg = [0] * n
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)
    deg[a] += 1
    deg[b] += 1

def bfs(root):
    res = [-1] * n
    res[root] = 0
    parent = [-1] * n
    stack = [root]
    while(stack):
        next = []
        while(stack):
            i = stack.pop()
            for j in links[i]:
                if res[j] != -1:
                    continue
                res[j] = res[i] + 1
                parent[j] = i
                next.append(j)
        stack, next = next,stack
    return res,parent

d,_ = bfs(0)
max_d = max(d)
root = -1
for i in range(n):
    if d[i] == max_d:
        root = i
        break

d,par = bfs(root)
max_d = max(d)
last = -1
for i in range(n):
    if d[i] == max_d:
        last = i
        break

search = []
if max_d % 2 == 1:
    x = last
    dx = max_d
    while(dx > (max_d+1)//2):
        x = par[x]
        dx -= 1
    
    search.append([x,par[x]])

else:
    x = last
    dx = max_d
    while(dx > max_d//2):
        x = par[x]
        dx -= 1
    search.append([x,x])
    for y in links[x]:
        search.append([x,y])

leaves = 1 << 70
for x,y in search:
    done = [0] * n
    done[x] = 1
    done[y] = 1
    res = 1
    if x == y:
        stack = [x]
    else:
        stack = [x,y]
        res = 2
    while(stack):
        next = []
        max_deg = 1
        while(stack):
            i = stack.pop()
            rem = 0
            for j in links[i]:
                if done[j] == 1:
                    rem += 1
                    continue
                done[j] = 1
                next.append(j)
            max_deg = max(max_deg,deg[i] - rem)
        stack,next = next,stack
        res *= max_deg
        # print(x,y,max_deg)
    
    leaves = min(leaves, res)

print((max_d+2)//2 ,leaves)
# print(d)
# print(links)
# print(deg)






