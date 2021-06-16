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

n = int(input())
s = [input() for _ in range(n)]

links = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == '1':
            links[i].append(j)

parents = [0] * n
for i in range(n):
    stack = [i]
    done = [0] * n
    done[i] = 1
    while stack:
        j = stack.pop()
        for k in links[j]:
            if done[k] == 1:
                continue
            done[k] = 1
            parents[k] += 1
            stack.append(k)

ans = 0
for pi in parents:
    ans += 1/(pi+1)
print(ans)


# import sys
 
# class Csr():
#     """
#     グラフの辺の情報を格納するデータ型。
#     CSR：Compressed Sparse Row　だが、ScipyなどのCSRの実装とは異なる。
#     // Reference:
#     // R. Tarjan,
#     // Depth-First Search and Linear Graph Algorithms
 
#     Parameters
#     ----------
#     n : int
#         グラフの頂点数
#     edges : list[x : int, e : list]
#         グラフの辺の情報
#         xは属する点の情報（有向辺のfromに当たる点の番号）
#         eは辺の情報（長さ・情報は可変）
 
#     Attributes
#     ----------
#     start : list
#     elist : list
#         点i(0-indexed)に紐づく辺の情報はelist[start[i]:start[i+1]]に格納される。
#         elistに持たせる情報は可変。（隣接点だけ、隣接点＋コスト、など）
#     """
 
#     def __init__(self, n: int, edges: list):
#         self.start = [0] * (n + 1)
#         self.elist = [0] * len(edges)
#         for e in edges:
#             self.start[e[0] + 1] += 1
#         for i in range(1, n + 1):
#             self.start[i] += self.start[i - 1]
#         counter = self.start[::]
#         for e in edges:
#             self.elist[counter[e[0]]] = e[1]
#             counter[e[0]] += 1
 
# class InternalScc():
#     """
#     有向グラフの強連結成分分解
#     https://atcoder.github.io/ac-library/document_ja/scc.html
 
#     Parameters
#     ----------
#     n : int
#         グラフの頂点数
 
#     Attributes
#     ----------
#     _n : int
#         グラフの頂点数
#     _edges : list[(from_, to))]
#         from_, toは全てint型
#         辺の始点がfrom_
#         辺の終点がto
 
#     Methods
#     -------
#     __init__(self, n=0)
#         初期化
#     num_verticles(self)
#         頂点数を返却する。
#         Returns
#         ----------
#         _n : int
#     add_edge(self, from_, to)
#         グラフに始点from_,終点toの有向辺を追加する。
#         Parameters
#         ----------
#         from_ : int
#             0 <= from_ < self._n
#         to : int
#             0 <= to < self._n
#     scc_ids(self)
#         強連結成分分解を行う関数。
#         Returns
#         ----------
#         [group_num, ids] : list
#             group_num : int
#                 グループ(強連結成分)の個数
#             ids : list
#                 各頂点のグループid
#     scc(self)
#         以下の条件を満たすような、「強連結成分となっている頂点のリスト」のリストを返却する。
#         ※トポロジカルソート済
#         Returns
#         ----------
#         groups : list
#             強連結成分の行数をKとすると、下記の形式となる。
#             [頂点(int)のリスト for _ in range(K)]
#     """
 
#     def __init__(self, n=0):
#         self._n = n
#         self._edges = []  # (int, edge)
 
#     def num_vertices(self):
#         return self._n
 
#     def add_edge(self, from_, to):
#         self._edges.append((from_, to))
 
#     def scc_ids(self):
#         g = Csr(self._n, self._edges)
#         now_ord, group_num = 0, 0
#         visited = []
#         low = [0] * self._n
#         ids = [0] * self._n
#         ord_ = [-1] * self._n
 
#         # 再帰関数の上限を変更
#         sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))
 
#         def _dfs(v):
#             nonlocal now_ord, group_num, visited, low, ids, ord_
#             low[v], ord_[v] = now_ord, now_ord
#             now_ord += 1
#             visited.append(v)
#             for i in range(g.start[v], g.start[v+1]):
#                 to = g.elist[i]
#                 if ord_[to] == -1:
#                     _dfs(to)
#                     low[v] = min(low[v], low[to])
#                 else:
#                     low[v] = min(low[v], ord_[to])
#             if low[v] == ord_[v]:
#                 while True:
#                     u = visited[-1]
#                     visited.pop()
#                     ord_[u] = self._n
#                     ids[u] = group_num
#                     if u == v:
#                         break
#                 group_num += 1
 
#         for i in range(self._n):
#             if ord_[i] == -1:
#                 _dfs(i)
#         ids = [group_num - 1 - x for x in ids]
#         return [group_num, ids]
 
#     def scc(self):
#         group_num, ids = self.scc_ids()
#         counts = [0] * group_num
#         groups = [[] for _ in range(group_num)]
#         for x in ids:
#             counts[x] += 1
#         for i in range(self._n):
#             groups[ids[i]].append(i)
#         return groups
      
# class Scc(InternalScc):
#     def add_edge(self, from_, to):
#         n = super().num_vertices()
#         assert 0 <= from_ < n
#         assert 0 <= to < n
#         super().add_edge(from_, to)

# n = int(input())
# s = [input() for _ in range(n)]

# scc = Scc(n)

# for i in range(n):
#     for j in range(n):
#         if s[i][j] == '1':
#             scc.add_edge(i,j)

# print(scc.scc())

# group_num, ids = scc.scc_ids()
# links = [[] for _ in range(group_num)]
# for i in range(n):
#     for j in range(n):
#         if s[i][j] == '1' and ids[i] != ids[j]:
#             links[ids[i]].append(ids[j])

# print(group_num)
# print(links)