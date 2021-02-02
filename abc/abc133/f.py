# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,q = map(int,readline().split())
data = list(map(int,read().split()))
abcd = data[:4*(n-1)]
xyuv = data[4*(n-1):]

root = 1
dbl_max = 20
dbl = [[0] * dbl_max for _ in range(n+1)]
depth = [0] * (n+1)
links = [[] for _ in range(n+1)]
it = iter(abcd)
for a,b,c,d in zip(it,it,it,it):
    links[a].append((b,c,d))
    links[b].append((a,c,d))

stack = [root]
while(stack):
    i = stack.pop()
    for j,c,d in links[i]:
        if(j==dbl[i][0]):
            continue
        dbl[j][0] = i
        depth[j] = depth[i]+1
        stack.append(j)

for i in range(1,dbl_max):
    for j in range(1,n+1):
        dbl[j][i] = dbl[dbl[j][i-1]][i-1]

def get_lca(x,y):
    if(depth[x] > depth[y]):
        x,y = y,x

    dif = depth[y]-depth[x]
    for i in range(dbl_max):
        if(dif==0):
            break
        if(dif>>i)&1:
            y = dbl[y][i]
            dif -= (1<<i)

    for i in range(dbl_max-1,-1,-1):
        if(dbl[x][i] != dbl[y][i]):
            x = dbl[x][i]
            y = dbl[y][i]

    if(x!=y):
        return dbl[x][0]
    else:
        return x

ans = [0] * q
query = [[] for _ in range(n+1)]
for i in range(q):
    x,y,u,v = xyuv[i*4:i*4+4]

    lca = get_lca(u,v)
    query[u].append((i,x,y,1))
    query[v].append((i,x,y,1))
    query[lca].append((i,x,y,-2))

tot = 0
c_cost = [[0,0] for _ in range(n)]
stack = []
for j,c,d in links[root]:
    stack.append((root,j,c,d,1))

while(stack):
    a,b,c,d,num = stack.pop()
    tot += d*num
    c_cost[c][0] += d*num
    c_cost[c][1] += num

    if(num==1):
        for qi,x,y,num_q in query[b]:
            ans[qi] += num_q * (tot - c_cost[x][0] + c_cost[x][1]*y)

        next = []
        for j,c,d in links[b]:
            if(j==dbl[b][0]):
                stack.append((b,j,c,d,-1))
            else:
                next.append((b,j,c,d,1))
        stack += next
    # print(c_cost)

print('\n'.join(map(str,ans)))

# for i in dbl:
#     print(i)
#
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j,get_lca(i,j))

'''
LCAを先に求めておく
すると、各クエリの答えは
d(u) + d(v) - 2*d(LCA) - (dc(u) + dc(v) - 2*dc(LCA)) + (dc_num(u) + dc_num(v) - 2*dc_num(LCA))*y

dはオイラーツアーしながら計算すればOK

'''
