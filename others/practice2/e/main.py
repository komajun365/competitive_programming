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

from heapq import heappop, heappush
class Csr():
    """
    グラフの辺の情報を格納するデータ型。
    CSR：Compressed Sparse Row　だが、ScipyなどのCSRの実装とは異なる。
    // Reference:
    // R. Tarjan,
    // Depth-First Search and Linear Graph Algorithms

    Parameters
    ----------
    n : int
        グラフの頂点数
    edges : list[x : int, e : list]
        グラフの辺の情報
        xは属する点の情報（有向辺のfromに当たる点の番号）
        eは辺の情報（長さ・情報は可変）

    Attributes
    ----------
    start : list
    elist : list
        点i(0-indexed)に紐づく辺の情報はelist[start[i]:start[i+1]]に格納される。
        elistに持たせる情報は可変。（隣接点だけ、隣接点＋コスト、など）
    """
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

class MinCostFlow:
    """
    最小費用流問題
    https://atcoder.github.io/ac-library/production/document_ja/mincostflow.html

    Parameters
    ----------
    n : int
        グラフの頂点数

    Attributes
    ----------
    _INF = 9_223_372_036_854_775_807 : int
        明に指定しなかった場合のフローの最大値
        longlong型の上限
    _n : int
        グラフの頂点数
    _edges : list[from_, to, cap, flow, cost]
        from_, to, cap, flow, costは全てint型
        辺の始点がfrom_
        辺の終点がto
        辺の容量がcap
        現在の流量がflow
        単位当たりコストがcost
    _log_max_n : int
        頂点数上限:=2**self._log_n、heapqの高速化用
    _bitmask : int
        同じくheapqの高速化用

    Methods
    -------
    __init__(self, n=0)
        初期化
    add_edge(self, from_, to, cap, cost)
        グラフに始点from_,終点to,容量cap,コストcostの辺を追加する。
        Parameters
        ----------
        from_ : int
            0 <= from_ < self._n
        to : int
            0 <= to < self._n
        cap : int
            0 <= cap
        cost : int
            0 <= cost
        Returns
        -------
        int
            何番目に追加した辺であるか、を返却する。
    get_edge(self, i)
        i番目に追加した辺の情報を返却する。
        Parameters
        ----------
        i : int
            0 <= i < len(self._edges)
        Returns
        -------
        [from_, to, cap, flow, cost] : list
    edges(self)
        全ての辺の情報を返却する。
        Returns
        -------
        result : list
            [[from_, to, cap, flow, cost] for _ in range(len(self._pos)]の形式
    flow(self, s, t, flow_limit=_INF)
        点sから点tへflow_limitを超えない範囲で流せるだけ流し、
        その流量とコストを返す
        Parameters
        ----------
        s,t : int
            0 <= i < len(self._n) かつ s != t
            sはフローの始点、tはフローの終点
        flow_limit : int
            流量の上限、指定しない場合は_INF
        Returns
        -------
        result : list
            [flow, cost]の形式
    slope(self, s, t, flow_limit=_INF)
        点sから点tへflow_limitを超えない範囲で流せるだけ流したとき、
        流量とコストの関係の折れ線を返却する。
        全ての xx について、流量 x の時の最小コストを g(x) とすると、
        (x, g(x)) は返り値を折れ線として見たものに含まれる。
        Parameters
        ----------
        s,t : int
            0 <= i < len(self._n) かつ s != t
            sはフローの始点、tはフローの終点
        flow_limit : int
            流量の上限、指定しない場合は_INF
        Returns
        -------
        result : list
            [[flow, cost] for _ in range(xxx)]の形式
    _slope(self, g, s, t, flow_limit)
        slopeの結果を求める内部関数
        Parameters
        ----------
        g : Csr
            グラフの辺の情報をCsrクラスで持ったもの。
        s,t : int
            0 <= i < len(self._n) かつ s != t
            sはフローの始点、tはフローの終点
        flow_limit : int
            流量の上限、指定しない場合は_INF
        Returns
        -------
        result : list
            [[flow, cost] for _ in range(xxx)]の形式
    """
    _INF = 9_223_372_036_854_775_807

    def __init__(self, n=0):
        self._n = n
        self._edges = []  # [from_, to, cap, flow, cost]
        self._log_max_n = 30
        self._bitmask = (1 << self._log_max_n) - 1

    def add_edge(self, from_, to, cap, cost):
        assert 0 <= from_ < self._n
        assert 0 <= to < self._n
        assert 0 <= cap
        assert 0 <= cost
        m = len(self._edges)
        self._edges.append([from_, to, cap, 0, cost])
        return m

    def get_edge(self, i):
        m = len(self._edges)
        assert 0 <= i < m
        return self._edges[i]

    def edges(self):
        return self._edges

    def flow(self, s, t, flow_limit=_INF):
        return self.slope(s, t, flow_limit)[-1]

    def slope(self, s, t, flow_limit=_INF):
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t

        m = len(self._edges)
        edge_idx = [0] * m

        degree = [0] * self._n
        redge_idx = [0] * m
        elist = []  # [e_num, edge=[to, rev, cap, cost]]
        for i in range(m):
            from_, to, cap, flow, cost = self._edges[i]
            edge_idx[i] = degree[from_]
            degree[from_] += 1
            redge_idx[i] = degree[to]
            degree[to] += 1
            elist.append([from_, [to, -1, cap - flow, cost]])
            elist.append([to, [from_, -1, flow, -cost]])
        g = Csr(self._n, elist)
        for i in range(m):
            from_, to, cap, flow, cost = self._edges[i]
            edge_idx[i] += g.start[from_]
            redge_idx[i] += g.start[to]
            g.elist[edge_idx[i]][1] = redge_idx[i]
            g.elist[redge_idx[i]][1] = edge_idx[i]

        result = self._slope(g, s, t, flow_limit)

        for i in range(m):
            cap = g.elist[edge_idx[i]][2]
            self._edges[i][3] = self._edges[i][2] - cap

        return result

    def _slope(self, g, s, t, flow_limit):
        dual_dist = [[0, 0] for _ in range(self._n)]
        prev_e = [0] * self._n

        def dual_ref():
            for i in range(self._n):
                dual_dist[i][1] = MinCostFlow._INF
            vis = [False] * self._n
            que_min = []
            que = []  # heapq

            # heap_r = 0
            dual_dist[s][1] = 0
            que_min.append(s)
            while que_min or que:
                v = 0
                if que_min:
                    v = que_min.pop()
                else:
                    v = heappop(que) & self._bitmask
                if vis[v]:
                    continue
                vis[v] = True
                if v == t:
                    break
                dual_v, dist_v = dual_dist[v]
                for i in range(g.start[v], g.start[v+1]):
                    to, rev, cap, cost_i = g.elist[i]
                    if cap <= 0:
                        continue
                    cost = cost_i - dual_dist[to][0] + dual_v
                    if dual_dist[to][1] - dist_v > cost:
                        dist_to = dist_v + cost
                        dual_dist[to][1] = dist_to
                        prev_e[to] = rev
                        if dist_to == dist_v:
                            que_min.append(to)
                        else:
                            heappush(que, (dist_to << self._log_max_n) + to)
            if not vis[t]:
                return False

            for v in range(self._n):
                if not vis[v]:
                    continue
                dual_dist[v][0] -= dual_dist[t][1] - dual_dist[v][1]
            return True

        flow = 0
        cost = 0
        prev_cost_per_flow = -1
        result = [[0, 0]]
        while flow < flow_limit:
            if not dual_ref():
                break
            c = flow_limit - flow
            v = t
            while v != s:
                to, rev = g.elist[prev_e[v]][:2]
                c = min(c, g.elist[rev][2])
                v = to
            v = t
            while v != s:
                to, rev = g.elist[prev_e[v]][:2]
                g.elist[prev_e[v]][2] += c
                g.elist[rev][2] -= c
                v = to
            d = - dual_dist[s][0]
            flow += c
            cost += c * d
            if prev_cost_per_flow == d:
                result.pop()
            result.append([flow, cost])
            prev_cost_per_flow = d
        return result

import sys
read = sys.stdin.buffer.read

n,k,*a = map(int,read().split())
n2 = n*2 + 2
s = n*2
t = s+1

inf = max(a)
mcf = MinCostFlow(n2)
mcf.add_edge(s, t, n**2, inf)
for i in range(n):
    mcf.add_edge(s, i, k, 0)
    mcf.add_edge(i+n, t, k, 0)

for i in range(n):
    for j in range(n):
        mcf.add_edge(i, j+n, 1, inf-a[i*n+j])

max_num = inf * n**2 - mcf.flow(s, t, n**2)[1]
res = [['.'] * n for _ in range(n)]

for from_, to, cap, flow, cost in mcf.edges():
    if from_ >= s or to >= s:
        continue
    if flow > 0:
        res[from_][to-n] = 'X'

print(max_num)
print('\n'.join(map(lambda x: ''.join(x), res)))

