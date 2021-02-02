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


n,m = map(int,readline().split())
d = [-1]
d += list(map(int,readline().split()))
uv = list(map(int,read().split()))

inf = 10**9
bw = ['?'] * (n+1)
edge_cost = [inf] * (m+1)

links = [dict() for _ in range(n+1)]
links_same =[[-1,-1] for _ in range(n+1)]
roots = set()
for i in range(1,m+1):
    u,v = uv[(i-1)*2 : i*2]
    if(d[u]==d[v]):
        links_same[u] = [v,i]
        links_same[v] = [u,i]
        roots.add(u)
        roots.add(v)
    elif(d[u] < d[v]):
        links[u][v] = i
    else:
        links[v][u] = i

for root in roots:
    if(bw[root] != '?'):
        continue

    stack = [root]
    root2 = links_same[root][0]
    if(bw[root2] == 'B'):
        bw[root] = 'W'
    elif(bw[root2] == 'W'):
        bw[root] = 'B'
    else:
        bw[root] = 'B'
        bw[root2] = 'W'
        stack.append(root2)
    edge_cost[links_same[root][1]] = d[root]

    while(stack):
        i = stack.pop()
        for j,e in links[i].items():
            if(bw[j] != '?'):
                continue
            bw[j] = bw[i]
            edge_cost[e] = d[j] - d[i]
            stack.append(j)

if(bw.count('?')!=1):
    print(-1)
    exit()

print(''.join(bw[1:]))
print('\n'.join(map(str,edge_cost[1:])))







'''
最小全域木なのか？
→　違う

隣り合っていて、コストが同じ頂点の組x,yを見つける
→　xを根として、子供に行くにつれて頂点コストが高くなるような増加部分木？を考える。
　 これらは全部同じ色にして、差分を辺のコストに割り当てていけばよい。
　　（yも同じ）

結局頂点のコストが低い方から大きい方への有向グラフとして考えると、
全ての点に根があることが重要。

根となる頂点のペアについて、コストが大きい方から処理していけばよいと思う。
順番関係ないかも。

使わなかった辺のコストはinfとしてよい。

'''
