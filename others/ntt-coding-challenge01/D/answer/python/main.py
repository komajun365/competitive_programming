# coding: utf-8

class Edge(object):

    def __init__(self, src, dst, cap, cost, rev):
        self.src = src
        self.dst = dst
        self.cap = cap
        self.cost = cost
        self.rev = rev

    def __repr__(self):
        return f'{self.src} -> {self.dst}\t' +\
               f'(cap: {self.cap}, cost: {self.cost}, rev: {self.rev})'


class Graph(object):

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dst, cap, cost):
        self.vertices[src].append(
            Edge(src, dst, cap, cost, len(self.vertices[dst])))
        self.vertices[dst].append(
            Edge(dst, src, 0, -cost, len(self.vertices[src]) - 1))

    def get_edges(self, vertex):
        return self.vertices[vertex]

    @property
    def V(self):
        return self.num_vertices

    def __getitem__(self, index):
        return self.vertices[index]

    def __repr__(self):
        ret = ''
        for v in self.vertices:
            for e in v:
                ret += repr(e) + '\n'
        return ret


def min_cost_flow_bellman_ford(G, s, t, f):
    # ベルマンフォード法
    res = 0
    inf = float('inf')
    prev_v = [0] * G.V
    prev_e = [0] * G.V

    while f > 0:
        dist = [inf] * G.V
        dist[s] = 0
        while True:
            update = False
            for v in range(G.V):
                if dist[s] == inf:
                    continue
                for i, e in enumerate(G[v]):
                # そのエッジの容量があって、コストが少ないならそのエッジの方が良い
                    if e.cap > 0 and dist[e.dst] > dist[v] + e.cost:
                        dist[e.dst] = dist[v] + e.cost
                        prev_v[e.dst] = v
                        prev_e[e.dst] = i
                        update = True
            if not update:
                break

        if dist[t] == inf:
            # これ以上流せない
            return res

        d = f
        v = t

        # 流せる最大流量を求める
        while v != s:
            d = min(d, G[prev_v[v]][prev_e[v]].cap)
            v = prev_v[v]

        # 流せるだけ流す
        f -= d

        # 終点まで流すためのコストを加算する
        res += d * dist[t]

        # 終点から始点まで逆向きに進んで各エッジの容量を更新する
        v = t
        while v != s:
            e = G[prev_v[v]][prev_e[v]]
            e.cap -= d
            G[v][e.rev].cap += d
            v = prev_v[v]

    return res


def min_cost_flow_dijkstra(G, s, t, f):
    # ポテンシャル付きダイクストラ法
    from heapq import heappop, heappush
    res = 0
    inf = float('inf')
    h = [0] * G.V
    prev_v = [0] * G.V
    prev_e = [0] * G.V
    while f > 0:
        dist = [inf] * G.V
        dist[s] = 0
        que = [(0, s)]
        while len(que) > 0:
            cost, src = heappop(que)
            if dist[src] < cost:
                continue
            for i, e in enumerate(G[src]):
                if e.cap > 0 and dist[e.dst] > dist[src] + e.cost + h[src] - h[e.dst]:
                    dist[e.dst] = dist[src] + e.cost + h[src] - h[e.dst]
                    prev_v[e.dst] = src
                    prev_e[e.dst] = i
                    heappush(que, (dist[e.dst], e.dst))
        if dist[t] == inf:
            # これ以上流せない
            return res

        for i in range(G.V):
            h[i] += dist[i]

        d = f
        v = t
        while v != s:
            d = min(d, G[prev_v[v]][prev_e[v]].cap)
            v = prev_v[v]
        f -= d
        res += d * h[t]
        v = t
        while v != s:
            e = G[prev_v[v]][prev_e[v]]
            e.cap -= d
            G[v][e.rev].cap += d
            v = prev_v[v]
    return res


def make_graph(hunts, guilds):
    # hunts: 狩場, guilds: ギルド
    # グラフ初期化
    G = Graph(len(hunts) + len(guilds) + 2)
    s = len(hunts) + len(guilds)
    t = len(hunts) + len(guilds) + 1

    # スタート地点から狩場までは
    # モンスター数だけキャパシティがある
    # コスト0で移動できる
    f = 0
    for i, (xi, yi, ei) in enumerate(hunts):
        G.add_edge(s, i, ei, 0)
        f += ei

    # ギルドからゴール地点までは
    # 結晶の貯蔵可能量までキャパシティがある
    # コスト0で移動できる
    total_capacity = 0
    for j, (vj, wj, cj) in enumerate(guilds):
        G.add_edge(j + len(hunts), t, cj, 0)
        total_capacity += cj

    # 狩場からギルドまでは
    # キャパシティは無限大=いくらでも移動できる
    # コストは |x_i - v_j| + |y_i - w_j| + 1 だけかかる
    total_cost = 0
    for i, (xi, yi, ei) in enumerate(hunts):
        for j, (vj, wj, cj) in enumerate(guilds):
            dij = abs(xi - vj) + abs(yi - wj) + 1
            total_cost += dij * cj
            G.add_edge(i, j + len(hunts), float('inf'), dij)

    return G, s, t, f


if __name__ == '__main__':
    M, N = map(int, input().split())
    hunts, guilds = [], []
    for i in range(M):
        xi, yi, ei = map(int, input().split())
        hunts.append([xi, yi, ei])
    for j in range(N):
        vi, wi, ci = map(int, input().split())
        guilds.append([vi, wi, ci])

    G, s, t, f = make_graph(hunts, guilds)

    method = 'dijkstra'
    if method == 'dijkstra':
        ans = min_cost_flow_dijkstra(G, s, t, f)
    else:
        ans = min_cost_flow_bellman_ford(G, s, t, f)
    print(ans)
