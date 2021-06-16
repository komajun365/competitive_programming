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

import sys
read = sys.stdin.buffer.read

# doubling
class LCA():
    def __init__(self, links, root):
        self.n = len(links)
        self.dbl = [[-1] for _ in range(self.n)]
        self.depth = [-1] * self.n
        self.depth[root] = 0
        stack = [root]
        while(stack):
            i = stack.pop()
            for j in links[i]:
                if(self.depth[j] != -1):
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
    
    def get_ancester(self, x, dep):
        assert self.depth[x] >= dep
        res = x
        dif = self.depth[x] - dep
        for bi in range(self.log_d):
            if(dif >> bi)&1:
                res = self.dbl[res][bi]
        return res


n,*data = map(int,read().split())
c = [i-1 for i in data[:n]]
ab = data[n:]

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

lca = LCA(links, 0)
stack_color = [[-1] for _ in range(n)]
stack = [0]
depth = [-1] * n
depth[0] = 0
ancester = [-1] * n
tp = []
while stack:
    i = stack.pop()
    if i >= 0:
        stack.append(~i)
        ci = c[i]
        # print(i,ci)
        # print(stack_color[ci])
        ancester[i] = stack_color[ci][-1]
        stack_color[ci].append(i)
        for j in links[i]:
            if depth[j] != -1:
                continue
            depth[j] = depth[i] + 1
            stack.append(j)
            tp.append(j)
    else:
        i = ~i
        ci = c[i]
        stack_color[ci].pop()

tp = tp[::-1]
dp = [0] * n
root_color = [0] * n
size = [1] * n
ans = [n*(n+1)//2] * n
for i in tp:
    ci = c[i]
    p = lca.dbl[i][0]
    cp = c[p]

    # 点ｉの先祖への処理
    anc = ancester[i]
    if anc == -1:
        root_color[ci] += size[i]
    else:
        anc_c = lca.get_ancester(i, depth[anc]+1)
        # print(i,anc_c)
        dp[anc_c] += size[i]

    # 1個上の色を使わない単純パスの数
    v_num = size[i] - dp[i]
    ans[cp] -= v_num * (v_num+1) //2

    # sizeの更新
    size[p] += size[i]
    # print(i,ci,ans)

root_color[c[0]] = n
# print(root_color)
# print(dp)

for i in range(n):
    v_num = n - root_color[i]
    ans[i] -= v_num * (v_num+1) //2

print('\n'.join(map(str,ans)))







