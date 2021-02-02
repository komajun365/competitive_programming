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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,*data = map(int,read().split())
ab = data[:(n-1)*2]
q = data[(n-1)*2]
tex = data[(n-1)*2 + 1:]

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

root = 0
depth = [-1] * n
depth[root] = 0
stack = [root]
child = [[] for _ in range(n)]
while(stack):
    i = stack.pop()
    for j in links[i]:
        if(depth[j] != -1):
            continue
        depth[j] = depth[i] + 1
        stack.append(j)
        child[i].append(j)


dp = [0] * n

it = iter(tex)
for t, e, x in zip(it,it,it):
    e -= 1
    a,b = ab[e*2:e*2+2]
    a -= 1
    b -= 1
    if(t==2):
        a,b = b,a
    if( depth[a] < depth[b] ):
        dp[root] += x
        dp[b] -= x
    else:
        dp[a] += x

stack = [root]
while(stack):
    i = stack.pop()
    for j in child[i]:
        dp[j] += dp[i]
        stack.append(j)

print(*dp, sep='\n')



# # doubling
# class LCA():
#     def __init__(self, links, root):
#         self.n = len(links)
#         self.dbl = [[-1] for _ in range(self.n)]
#         self.depth = [-1] * self.n
#         self.depth[root] = 0
#         stack = [root]
#         while(stack):
#             i = stack.pop()
#             for j in links[i]:
#                 if(self.depth[j] != -1):
#                     continue
#                 self.depth[j] = self.depth[i] + 1
#                 self.dbl[j][0] = i
#                 stack.append(j)
        
#         self.log_d = (max(self.depth)).bit_length()
#         for j in range(self.log_d - 1):
#             for i in range(n):
#                 ancestor = self.dbl[i][j]
#                 self.dbl[i].append(self.dbl[ancestor][j])
        
#     def lca(self, x, y):
#         assert (self.depth[x] >= 0) and (self.depth[y] >= 0)
#         if(self.depth[x] < self.depth[y]):
#             x,y = y,x
#         dif = self.depth[x] - self.depth[y]
#         for bi in range(self.log_d):
#             if(dif >> bi)&1:
#                 x = self.dbl[x][bi]
        
#         if(x == y):
#             return x
#         for bi in range(self.log_d-1, -1, -1):
#             if(self.dbl[x][bi] != self.dbl[y][bi]):
#                 x = self.dbl[x][bi]
#                 y = self.dbl[y][bi]
#         return self.dbl[x][0]