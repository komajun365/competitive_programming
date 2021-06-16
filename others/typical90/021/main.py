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

class csr():
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


class internal_scc_graph():
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

    def scc(self):
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups = [[] for _ in range(group_num)]
        for i, x in enumerate(ids[1]):
            groups[x].append(i)

        return groups


class scc_graph():
    def __init__(self, n: int):
        self.__internal = internal_scc_graph(n)

    def add_edge(self, from_: int, to: int):
        n = self.__internal.num_vertices()
        assert (0 <= from_) & (from_ < n)
        assert (0 <= to) & (to < n)
        self.__internal.add_edge(from_, to)

    def scc(self):
        return self.__internal.scc()

import sys
read = sys.stdin.buffer.read

n,m,*ab = map(int,read().split())

scc = scc_graph(n)
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    scc.add_edge(a,b)

res = scc.scc()
ans = 0
for ri in res:
    l = len(ri)
    ans += l*(l-1)//2
print(ans)