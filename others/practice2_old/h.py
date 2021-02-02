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

class csr:
    def __init__(self, n: int, edges: list):
        self.start = [0] * (n + 1)
        self.elist = [0] * len(edges)
        for e in edges:
            self.start[e[0] + 1] += 1
        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]
        counter = self.start[::]
        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1


class internal_scc_graph:
    def __init__(self, n: int = 0):
        self.__n = n
        self.__edges = []

    def num_vertices(self):
        return self.__n

    def add_edge(self, from_: int, to: int):
        self.__edges.append([from_, to])

    def scc_ids(self):
        g = csr(self.__n, self.__edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self.__n
        ord = [-1] * self.__n
        ids = [0] * self.__n
        parent = [-1] * self.__n

        for root in range(self.__n):
            if(ord[root] == -1):
                stack = []
                stack.extend([root] * 2)
                while(stack):
                    v = stack.pop()
                    if(ord[v] == -1):
                        visited.append(v)
                        low[v] = now_ord
                        ord[v] = now_ord
                        now_ord += 1
                        for i in range(g.start[v], g.start[v + 1]):
                            to = g.elist[i]
                            if(ord[to] == -1):
                                stack.extend([to] * 2)
                                parent[to] = v
                            else:
                                low[v] = min(low[v], ord[to])
                    else:
                        if(low[v] == ord[v]):
                            while(True):
                                u = visited.pop()
                                ord[u] = self.__n
                                ids[u] = group_num
                                if(u == v):
                                    break
                            group_num += 1
                        if(parent[v] != -1):
                            low[parent[v]] = min(low[parent[v]], low[v])

        for i, x in enumerate(ids):
            ids[i] = group_num - 1 - x
        return [group_num, ids]


class two_sat:
    def __init__(self, n: int = 0):
        self.__n = n
        self.__answer = [0] * n
        self.__scc = internal_scc_graph(2 * n)

    def add_clause(self, i: int, f: bool, j: int, g: bool):
        assert (0 <= i) & (i < self.__n)
        assert (0 <= j) & (j < self.__n)
        self.__scc.add_edge(2 * i + (1 - f), 2 * j + g)
        self.__scc.add_edge(2 * j + (1 - g), 2 * i + f)

    def satisfiable(self):
        id = self.__scc.scc_ids()[1]
        for i in range(self.__n):
            if(id[2 * i] == id[2 * i + 1]):
                return False
            self.__answer[i] = (id[2 * i] < id[2 * i + 1])
        return True

    def answer(self):
        return self.__answer

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,d = map(int,readline().split())
xy = [list(map(int, i.split())) for i in readlines()]

ts = two_sat(n)
for i in range(n-1):
    for j in range(i+1,n):
        for ii,jj in zip([0,0,1,1],[0,1,0,1]):
            if(abs(xy[i][ii] - xy[j][jj]) < d):
                ts.add_clause(i, 1-ii, j, 1-jj)

if(ts.satisfiable()):
    print('Yes')
else:
    print('No')
    exit()

ans = []
for i,tf in enumerate(ts.answer()):
    ans.append(xy[i][tf])
print('\n'.join(map(str,ans)))
