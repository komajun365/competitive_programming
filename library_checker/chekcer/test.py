# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

# lowlink

import sys
read = sys.stdin.buffer.read
import random

# n,m,*ab = map(int,read().split())

# links = [[] for _ in range(n)]
# it = iter(ab)
# for a,b in zip(it,it):
#     links[a].append(b)
#     links[b].append(a)

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

def solve(n,m,ab):
    links = [[] for _ in range(n)]
    it = iter(ab)
    for a,b in zip(it,it):
        links[a].append(b)
        links[b].append(a)
    components,new_edges = two_edge_connected_componets(links)
    # return components
    group = dict()
    for i,ci in enumerate(components):
        if ci in group:
            group[ci].append(i)
        else:
            group[ci] = [i]

    # print(len(group))
    ans = []
    for val in group.values():
        tmp = [len(val)]
        for i in val:
            tmp.append(i)
        ans.append(' '.join(map(str,tmp)))
    # print('\n'.join(ans))
    return ans

# order,low,roots,child = lowlink(links)
# print(order)
# print(low)
# print(roots)
# print(child)

# print(get_articulation(links))
    
# components,new_edges = two_edge_connected_componets(links)
# print(components)
# print(new_edges)

# print(get_bridge(links))

class LowLink:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.dfstree = [[] for _ in range(n)]
        self.par = [-1] * n
        self.ord = [-1] * n
        self.low = [-1] * n
        self.roots = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def build(self):
        k = 0
        self.edge_cnt = {}
        for v in range(self.n):
            for nxt_v in self.graph[v]:
                self.edge_cnt[v, nxt_v] = self.edge_cnt.get((v, nxt_v), 0) + 1
        idxs = [0] * self.n
        for v in range(self.n):
            if self.ord[v] == -1:
                self.roots.add(v)
                k = self.dfs(v, idxs, k)

    def dfs(self, root, idxs, k):
        stack = [root]
        while stack:
            v = stack[-1]
            if v < 0:
                v = ~v
                par_v = self.par[v]
                self.low[par_v] = min(self.low[par_v], self.low[v])
                stack.pop()
                continue
            idx = idxs[v]
            if self.ord[v] == -1:
                self.ord[v] = self.low[v] = k
                k += 1
            if idx < len(self.graph[v]):
                nxt_v = self.graph[v][idx]
                idxs[v] += 1
                if nxt_v == self.par[v] and self.edge_cnt[v, nxt_v] == 1:
                    continue 
                elif self.ord[nxt_v] == -1:
                    self.dfstree[v].append(nxt_v)
                    self.dfstree[nxt_v].append(v)
                    self.par[nxt_v] = v
                    stack.append(~nxt_v)
                    stack.append(nxt_v)
                else:
                    self.low[v] = min(self.low[v], self.ord[nxt_v])
            else:
                stack.pop()
        return k

    def two_edge_connected_components(self):
        self.group = [-1] * self.n
        self.lb = 0
        for v in range(self.n):
            if self.group[v] != -1:
                continue
            self.group[v] = self.lb
            stack = [v]
            while stack:
                v = stack.pop()
                for nxt_v in self.graph[v]:
                    if self.ord[v] < self.low[nxt_v] or self.ord[nxt_v] < self.low[v]:
                        continue
                    if self.group[nxt_v] != -1:
                        continue
                    self.group[nxt_v] = self.lb
                    stack.append(nxt_v)
            self.lb += 1

def solve2(n,m,ab):
    ll = LowLink(n)
    it = iter(ab)
    for a,b in zip(it,it):
        ll.add_edge(a, b)

    ll.build()
    ll.two_edge_connected_components()
    # print(ll.group)
    # return ll.group

    res = [[] for i in range(ll.lb)]
    for v, lb in enumerate(ll.group):
        res[lb].append(v)
    
    ans = []
    for val in res:
        tmp = [len(val)]
        tmp += val
        ans.append(' '.join(map(str,tmp)))
    return ans

for _ in range(100000):
    n = random.randint(1,100)
    m = random.randint(1,200)
    ab = []
    for _ in range(m):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        ab += [a,b]
    
    res1 = solve(n,m,ab)
    res2 = solve2(n,m,ab)
    if res1 != res2:
        print(n,m)
        print(ab)
        print(res1)
        print(res2)
        exit()
