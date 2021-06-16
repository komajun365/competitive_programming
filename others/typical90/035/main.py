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

# doubling
class LCA():
    def __init__(self, links, root):
        self.n = len(links)
        self.dbl = [[-1] for _ in range(self.n)]
        self.depth = [-1] * self.n
        self.depth[root] = 0
        self.order = []
        stack = [root]
        while stack:
            i = stack.pop()
            self.order.append(i)
            for j in links[i]:
                if self.depth[j] != -1:
                    continue
                self.depth[j] = self.depth[i] + 1
                self.dbl[j][0] = i
                stack.append(j)
        
        self.log_d = (max(self.depth)).bit_length()
        for j in range(self.log_d - 1):
            for i in range(self.n):
                ancestor = self.dbl[i][j]
                self.dbl[i].append(self.dbl[ancestor][j])
        
    def lca(self, x, y):
        assert (self.depth[x] >= 0) and (self.depth[y] >= 0)
        if(self.depth[x] < self.depth[y]):
            x,y = y,x
        dif = self.depth[x] - self.depth[y]
        for bi in range(self.log_d):
            if(dif >> bi)&1:
                x = self.dbl[x][bi]
        
        if(x == y):
            return x
        for bi in range(self.log_d-1, -1, -1):
            if(self.dbl[x][bi] != self.dbl[y][bi]):
                x = self.dbl[x][bi]
                y = self.dbl[y][bi]
        return self.dbl[x][0]

import sys
read = sys.stdin.buffer.read

n,*data = map(int,read().split())
ab = data[:2*(n-1)]
q = data[2*(n-1)]
kv = data[2*(n-1)+1:]

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

lca = LCA(links, 0)
sort_num = [0] * n
for i,oi in enumerate(lca.order):
    sort_num[oi] = i

ans = []
idx = 0
for _ in range(q):
    k = kv[idx]
    v = [i-1 for i in kv[idx+1:idx+1+k]]
    idx += 1+k

    v.sort(key=lambda x: sort_num[x])
    
    tmp = 0
    for i in range(k):
        x = v[i-1]
        y = v[i]
        lca_xy = lca.lca(x,y)
        tmp += lca.depth[x] + lca.depth[y] - lca.depth[lca_xy] * 2
    
    tmp //= 2
    ans.append(tmp)

print('\n'.join(map(str,ans)))



