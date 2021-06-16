# coding: utf-8

from .main import Edge


class Graph(object):

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dst, cap, cost):
        self.vertices[src].append(
            Edge(src, dst, cap, cost, len(self.vertices[dst])))

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


def min_cost_flow_greedy(G, s, t, f):
    # 貪欲法: 単純にコストが最小のパスにフローを流し続ける
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
        while v != s:
            d = min(d, G[prev_v[v]][prev_e[v]].cap)
            v = prev_v[v]

        f -= d
        res += d * dist[t]
        v = t
        while v != s:
            e = G[prev_v[v]][prev_e[v]]
            e.cap -= d
            v = prev_v[v]

    return res


def make_graph(hunts, guilds):
    G = Graph(len(hunts) + len(guilds) + 2)
    s = len(hunts) + len(guilds)
    t = len(hunts) + len(guilds) + 1

    f = 0
    for i, (xi, yi, ei) in enumerate(hunts):
        G.add_edge(s, i, ei, 0)
        f += ei

    total_capacity = 0
    for j, (vj, wj, cj) in enumerate(guilds):
        G.add_edge(j + len(hunts), t, cj, 0)
        total_capacity += cj

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

    ans = min_cost_flow_greedy(G, s, t, f)
    print(ans)
