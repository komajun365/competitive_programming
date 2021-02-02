from heapq import heappop, heappush, heapify

class MinCostFlow():
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.pos = []

    def add_edge(self, fr, to, cap, cost):
        #assert 0 <= fr < self.n
        #assert 0 <= to < self.n
        m = len(self.pos)
        self.pos.append((fr, len(self.graph[fr])))
        self.graph[fr].append([to, len(self.graph[to]), cap, cost])
        self.graph[to].append([fr, len(self.graph[fr]) - 1, 0, -cost])
        return m

    def get_edge(self, idx):
        #assert 0 <= idx < len(self.pos)
        to, rev, cap, cost = self.graph[self.pos[idx][0]][self.pos[idx][1]]
        rev_to, rev_rev, rev_cap, rev_cost = self.graph[to][rev]
        return self.pos[idx][0], to, cap + rev_cap, rev_cap, cost

    def edges(self):
        for i in range(len(self.pos)):
            yield self.get_edge(i)

    def dual_ref(self, s, t):
        dist = [2**63 - 1] * self.n
        dist[s] = 0
        vis = [0] * self.n
        self.pv = [-1] * self.n
        self.pe = [-1] * self.n
        queue = []
        heappush(queue, (0, s))
        while queue:
            k, v = heappop(queue)
            if vis[v]: continue
            vis[v] = True
            if v == t: break
            for i in range(len(self.graph[v])):
                to, rev, cap, cost = self.graph[v][i]
                if vis[to] or cap == 0: continue
                cost += self.dual[v] - self.dual[to]
                if dist[to] - dist[v] > cost:
                    dist[to] = dist[v] + cost
                    self.pv[to] = v
                    self.pe[to] = i
                    heappush(queue, (dist[to], to))
        if not vis[t]: return False
        for v in range(self.n):
            if not vis[v]: continue
            self.dual[v] -= dist[t] - dist[v]
        return True

    def flow(self, s, t):
        return self.flow_with_limit(s, t, 2**63 - 1)

    def flow_with_limit(self, s, t, limit):
        return self.slope_with_limit(s, t, limit)[-1]

    def slope(self, s, t):
        return self.slope_with_limit(s, t, 2**63 - 1)

    def slope_with_limit(self, s, t, limit):
        #assert 0 <= s < self.n
        #assert 0 <= t < self.n
        #assert s != t
        flow = 0
        cost = 0
        prev_cost = -1
        res = [(flow, cost)]
        self.dual = [0] * self.n
        while flow < limit:
            if not self.dual_ref(s, t): break
            c = limit - flow
            v = t
            while v != s:
                c = min(c, self.graph[self.pv[v]][self.pe[v]][2])
                v = self.pv[v]
            v = t
            while v != s:
                to, rev, cap, _ = self.graph[self.pv[v]][self.pe[v]]
                self.graph[self.pv[v]][self.pe[v]][2] -= c
                self.graph[v][rev][2] += c
                v = self.pv[v]
            d = -self.dual[s]
            flow += c
            cost += c * d
            if prev_cost == d:
                res.pop()
            res.append((flow, cost))
            prev_cost = cost
        return res
