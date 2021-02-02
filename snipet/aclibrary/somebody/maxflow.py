from collections import deque

class MaxFlow():
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.pos = []

    def add_edge(self, fr, to, cap):
        #assert 0 <= fr < self.n
        #assert 0 <= to < self.n
        #assert 0 <= cap
        m = len(self.pos)
        self.pos.append((fr, len(self.graph[fr])))
        self.graph[fr].append([to, len(self.graph[to]), cap])
        self.graph[to].append([fr, len(self.graph[fr]) - 1, 0])
        return m

    def get_edge(self, idx):
        #assert 0 <= idx < len(self.pos)
        to, rev, cap = self.graph[self.pos[idx][0]][self.pos[idx][1]]
        rev_to, rev_rev, rev_cap = self.graph[to][rev]
        return rev_to, to, cap + rev_cap, rev_cap

    def edges(self):
        m = len(self.pos)
        for i in range(m):
            yield self.get_edge(i)

    def change_edge(self, idx, new_cap, new_flow):
        #assert 0 <= idx < len(self.pos)
        #assert 0 <= new_flow <= new_cap
        to, rev, cap = self.graph[self.pos[idx][0]][self.pos[idx][1]]
        self.graph[self.pos[idx][0]][self.pos[idx][1]][2] = new_cap - new_flow
        self.graph[to][rev][2] = new_flow

    def dfs(self, s, v, up):
        if v == s: return up
        res = 0
        lv = self.level[v]
        for i in range(self.iter[v], len(self.graph[v])):
            to, rev, cap = self.graph[v][i]
            if lv <= self.level[to] or self.graph[to][rev][2] == 0: continue
            d = self.dfs(s, to, min(up - res, self.graph[to][rev][2]))
            if d <= 0: continue
            self.graph[v][i][2] += d
            self.graph[to][rev][2] -= d
            res += d
            if res == up: break
            self.iter[v] += 1
        return res

    def max_flow(self, s, t):
        return self.max_flow_with_limit(s, t, 2**63 - 1)

    def max_flow_with_limit(self, s, t, limit):
        #assert 0 <= s < self.n
        #assert 0 <= t < self.n
        flow = 0
        while flow < limit:
            self.level = [-1] * self.n
            self.level[s] = 0
            queue = deque()
            queue.append(s)
            while queue:
                v = queue.popleft()
                for to, rev, cap in self.graph[v]:
                    if cap == 0 or self.level[to] >= 0: continue
                    self.level[to] = self.level[v] + 1
                    if to == t: break
                    queue.append(to)
            if self.level[t] == -1: break
            self.iter = [0] * self.n
            while flow < limit:
                f = self.dfs(s, t, limit - flow)
                if not f: break
                flow += f
        return flow

    def min_cut(self, s):
        visited = [0] * self.n
        queue = deque()
        queue.append(s)
        while queue:
            p = queue.popleft()
            visited[p] = True
            for to, rev, cap in self.graph[p]:
                if cap and not visited[to]:
                    visited[to] = True
                    queue.append(to)
        return visited
