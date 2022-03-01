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

def lowlink(links):
    n = len(links)
    order = [-1] * n
    low = [n] * n
    parent = [-1] * n
    child = [[] for _ in range(n)]
    roots = set()
    x = 0
    for root in range(n):
        if order[root] != -1:
            continue
        roots.add(root)
        stack = [root]
        parent[root] = -2
        while stack:
            i = stack.pop()
            if i >= 0:
                if order[i] != -1:
                    continue
                order[i] = x
                low[i] = x
                x += 1
                if i != root:
                    child[parent[i]].append(i)
                stack.append(~i)
                check_p = 0
                for j in links[i]:
                    if j == parent[i] and check_p == 0:
                        check_p += 1
                        continue
                    elif order[j] != -1:
                        low[i] = min(low[i], order[j])
                    else:
                        parent[j] = i
                        stack.append(j)
            else:
                i = ~i
                if i == root:
                    continue
                p = parent[i]
                low[p] = min(low[p], low[i])
    
    return order,low,roots,child

def get_articulation(links):
    n = len(links)
    order,low,roots,child = lowlink(links)
    articulation = [0] * n
    for i in range(n):
        if i in roots:
            if len(child[i]) >= 2:
                articulation[i] = 1
            continue
        for j in child[i]:
            if order[i] <= low[j]:
                articulation[i] = 1
                break
    
    return articulation

def get_bridge(links):
    n = len(links)
    order,low,roots,child = lowlink(links)
    bridge = []
    for root in roots:
        stack = [root]
        while stack:
            i = stack.pop()
            for j in child[i]:
                if order[i] < low[j]:
                    bridge.append([i,j])
                stack.append(j)
    
    return bridge

n,*xy = map(int,read().split())

for i in range(2*n+1):
    xy[i*2+1] += 2*n+1

n2 = 4*n+3
links = [[] for _ in range(n2)]
dic = dict()
for i in range(2*n+1):
    x,y = xy[i*2:i*2+2]
    links[x].append(y)
    links[y].append(x)
    dic[(x << 20 )+ y] = i
    dic[(y << 20 )+ x] = i

tp = []
parent = [-1] * n2
for i in range(n2):
    if parent[i] != -1:
        continue
    
    parent[i] = -2
    lines = 0
    stack = [i]
    tp0 = [i]

    while stack:
        stack2 = []
        while stack:
            j = stack.pop()
            lines += len(links[j])
            for k in links[j]:
                if parent[k] != -1:
                    continue
                parent[k] = j
                stack2.append(k)
                tp0.append(k)
        stack,stack2 = stack2,stack
    
    lines //= 2
    if lines % 2 == 1:
        if len(tp) != 0:
            ans = ['NG'] * (2*n+1)
            print('\n'.join(ans))
            exit()
        tp = tp0[::-1]

res = get_bridge(links)
bridges = set()
for x,y in res:
    bridges.add((x<<20)+y)
    bridges.add((y<<20)+x)

ans = ['NG'] * (2*n+1)

for i in tp:
    for j in links[i]:
        num = (i<<20) + j
        ans[dic[num]] = 'OK'


dp = [0] * n2
for i in tp:
    p = parent[i]
    if p == -2:
        break
    num = (i<<20) + p
    if num in bridges:
        lines = dp[i] + len(links[i]) - 1
        lines //= 2
        if lines % 2 == 1:
            ans[dic[num]] = 'NG'
    
    dp[p] += dp[i] + len(links[i])

print('\n'.join(ans))
