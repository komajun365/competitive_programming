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


import sys
class InternalScc():
    """
    有向グラフの強連結成分分解
    https://atcoder.github.io/ac-library/document_ja/scc.html

    Parameters
    ----------
    n : int
        グラフの頂点数

    Attributes
    ----------
    _n : int
        グラフの頂点数
    _edges : list[(from_, to))]
        from_, toは全てint型
        辺の始点がfrom_
        辺の終点がto

    Methods
    -------
    __init__(self, n=0)
        初期化
    num_verticles(self)
        頂点数を返却する。
        Returns
        ----------
        _n : int
    add_edge(self, from_, to)
        グラフに始点from_,終点toの有向辺を追加する。
        Parameters
        ----------
        from_ : int
            0 <= from_ < self._n
        to : int
            0 <= to < self._n
    scc_ids(self)
        強連結成分分解を行う関数。
        Returns
        ----------
        [group_num, ids] : list
            group_num : int
                グループ(強連結成分)の個数
            ids : list
                各頂点のグループid
    scc(self)
        以下の条件を満たすような、「強連結成分となっている頂点のリスト」のリストを返却する。
        ※トポロジカルソート済
        Returns
        ----------
        groups : list
            強連結成分の行数をKとすると、下記の形式となる。
            [頂点(int)のリスト for _ in range(K)]
    """

    def __init__(self, n=0):
        self._n = n
        self._edges = []  # (int, edge)

    def num_vertices(self):
        return self._n

    def add_edge(self, from_, to):
        self._edges.append((from_, to))

    def scc_ids(self):
        g = Csr(self._n, self._edges)
        now_ord, group_num = 0, 0
        visited = []
        low = [0] * self._n
        ids = [0] * self._n
        ord_ = [-1] * self._n

        # 再帰関数の上限を変更
        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))

        def _dfs(v):
            nonlocal now_ord, group_num, visited, low, ids, ord_
            low[v], ord_[v] = now_ord, now_ord
            now_ord += 1
            visited.append(v)
            for i in range(g.start[v], g.start[v+1]):
                to = g.elist[i]
                if ord_[to] == -1:
                    _dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], ord_[to])
            if low[v] == ord_[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    ord_[u] = self._n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self._n):
            if ord_[i] == -1:
                _dfs(i)
        ids = [group_num - 1 - x for x in ids]
        return [group_num, ids]

    def scc(self):
        group_num, ids = self.scc_ids()
        counts = [0] * group_num
        groups = [[] for _ in range(group_num)]
        for x in ids:
            counts[x] += 1
        for i in range(self._n):
            groups[ids[i]].append(i)
        return groups

class TwoSAT:
    """
    2-SATを解きます。
    https://atcoder.github.io/ac-library/master/document_ja/twosat.html

    Parameters
    ----------
    n : int
        変数の総数

    Attributes
    ----------
    _n : int
        変数の総数
    _answer : list[bool]
        satisfiable()実行後、
        条件を満たす割り当てが存在した場合に割り当てを格納する。
    _scc : INternalScc
        2-SAT問題を解くための内部グラフ

    Methods
    -------
    __init__(self, n=0)
        初期化
    add_clause(self, i, f, j, g)
        x_i = f もしくは x_j = g というクローズを追加する。
        Parameters
        ----------
        i : int
            0 <= i < self._n
        f : bool
        j : int
            0 <= j < self._n
        g : bool
    satisfiable(self)
        現在のクローズに対して、条件を満たす割り当てが存在するか判定する。
        また、割り当てが存在するとき_answerを更新する。
        Returns
        -------
        res : bool
            割り当てが存在すればTrue,しなければFalse
    answer(self)
        satisfiable()実行後、
        条件を満たす割り当てが存在した場合に割り当てを返却する。
        satisfiable()未実施、あるいは割り当てが存在しなかった場合の返却値は未定義。
        Returns
        -------
        _answer : list[bool]
    """
    def __init__(self, n=0):
        self._n = n
        self._answer = [0] * n
        self._scc = InternalScc(2 * n)

    def add_clause(self, i, f, j, g):
        assert 0 <= i < self._n
        assert 0 <= j < self._n
        self._scc.add_edge(2 * i + (1 - f), 2 * j + g)
        self._scc.add_edge(2 * j + (1 - g), 2 * i + f)

    def satisfiable(self):
        id = self._scc.scc_ids()[1]
        for i in range(self._n):
            if id[2 * i] == id[2 * i + 1]:
                return False
            self._answer[i] = (id[2 * i] < id[2 * i + 1])
        return True

    def answer(self):
        return self._answer

# import sys
read = sys.stdin.buffer.read

n,d,*data = map(int,read().split())
x = data[::2]
y = data[1::2]

ts = TwoSAT(n)
for i in range(n-1):
    for j in range(i+1,n):
        if abs(x[i] - x[j]) < d:
            ts.add_clause(i, False, j, False)
        if abs(x[i] - y[j]) < d:
            ts.add_clause(i, False, j, True)
        if abs(y[i] - x[j]) < d:
            ts.add_clause(i, True, j, False)
        if abs(y[i] - y[j]) < d:
            ts.add_clause(i, True, j, True)

if not ts.satisfiable():
    print('No')
    exit()

print('Yes')

ans = ts.answer()
points = []
for i,bi in enumerate(ans):
    if bi:
        points.append(str(x[i]))
    else:
        points.append(str(y[i]))
print('\n'.join(points))