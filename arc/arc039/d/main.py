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


class LCA():
    def __init__(self, links, root):
        self.n = len(links)
        self.dbl = [[-1] for _ in range(self.n)]
        self.depth = [-1] * self.n
        self.depth[root] = 0
        stack = [root]
        while(stack):
            i = stack.pop()
            for j in links[i]:
                if(self.depth[j] != -1):
                    continue
                self.depth[j] = self.depth[i] + 1
                self.dbl[j][0] = i
                stack.append(j)
        
        self.log_d = (max(self.depth)).bit_length()
        for j in range(self.log_d - 1):
            for i in range(self.n):
                ancestor = self.dbl[i][j]
                self.dbl[i].append(self.dbl[ancestor][j])
        
    def lca(self, x, y):
        assert (self.depth[x] >= 0) and (self.depth[y] >= 0)
        if(self.depth[x] < self.depth[y]):
            x,y = y,x
        dif = self.depth[x] - self.depth[y]
        for bi in range(self.log_d):
            if(dif >> bi)&1:
                x = self.dbl[x][bi]
        
        if(x == y):
            return x
        for bi in range(self.log_d-1, -1, -1):
            if(self.dbl[x][bi] != self.dbl[y][bi]):
                x = self.dbl[x][bi]
                y = self.dbl[y][bi]
        return self.dbl[x][0]

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

def two_edge_connected_componets(links):
    n = len(links)
    order,low,roots,child = lowlink(links)
    
    components = [-1] * n
    new_edges = []
    x = 0
    for root in roots:
        components[root] = x
        stack = [root]
        while stack:
            i = stack.pop()
            for j in child[i]:
                if order[i] < low[j]:
                    x += 1
                    components[j] = x
                    new_edges.append([components[i],x])
                else:
                    components[j] = components[i]
                stack.append(j)        
        x += 1
    
    return components,new_edges

import sys
from collections import deque
read = sys.stdin.buffer.read

n,m,*data = map(int,read().split())
xy = data[:2*m]
q = data[2*m]
abc = data[2*m+1:]

links = [[] for _ in range(n)]
it = iter(xy)
for x,y in zip(it,it):
    x -= 1
    y -= 1
    links[x].append(y)
    links[y].append(x)

# order,low,roots,child = lowlink(links)
# print(order)
# print(low)
# print(roots)
# print(child)

# print(get_articulation(links))
    
# components,new_edges = two_edge_connected_componets(links)
# print(components)
# print(new_edges)

components,new_edges = two_edge_connected_componets(links)

n2 = max(components) + 1
links = [[] for _ in range(n2)]
for x,y in new_edges:
    links[x].append(y)
    links[y].append(x)

lca = LCA(links, 0)

ans = []
it = iter(abc)
for a,b,c in zip(it,it,it):
    a = components[a-1]
    b = components[b-1]
    c = components[c-1]
    # print(a,b,c)
    if a==b or b==c:
        ans.append('OK')
        continue
    if a==c:
        ans.append('NG')
        continue

    lca_ac = lca.lca(a,c)
    if lca_ac == a:
        lca_bc = lca.lca(b,c)
        if lca_bc == b and lca.depth[a] < lca.depth[b]:
            ans.append('OK')
        else:
            ans.append('NG')
    elif lca_ac == c:
        lca_ab = lca.lca(a,b)
        if lca_ab== b and lca.depth[c] < lca.depth[b]:
            ans.append('OK')
        else:
            ans.append('NG')
    else:
        lca_bc = lca.lca(b,c)
        lca_ab = lca.lca(a,b)
        if (lca_ab == b or lca_bc == b) and lca.depth[b] >= lca.depth[lca_ac]:
            ans.append('OK')
        else:
            ans.append('NG')

print('\n'.join(ans))

# print(gm2)
# print(links)
# print(lca.dbl)
# print(lca.depth)

