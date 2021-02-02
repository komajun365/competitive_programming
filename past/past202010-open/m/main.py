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

n,q,*data = map(int,read().split())
ab = data[:2*(n-1)]
uvc = data[2*(n-1):]

links = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = ab[i*2:i*2+2]
    links[a].append((b << 20) + i)
    links[b].append((a << 20) + i)

depth = [-1] * (n+1)
parent = [[-1,-1] for _ in range(n+1)]
root = 1
depth[root] = 0
stack = [root]
while(stack):
    i = stack.pop()
    for num in links[i]:
        j,e = divmod(num,1<<20)
        if(depth[j] != -1):
            continue
        depth[j] = depth[i] + 1
        parent[j] = [i,e]
        stack.append(j)

ans = [0] * (n-1)
jump = list(range(n+1))

for i in range(q-1,-1,-1):
    u,v,c = uvc[i*3:i*3+3]
    done = []
    while(u != v):
        if(depth[u] < depth[v]):
            u,v = v,u
        if(jump[u] != u):
            done.append(u)
            u = jump[u]
        else:
            j,e = parent[u]
            ans[e] = c
            done.append(u)
            u = j
    for i in done:
        jump[i] = u

print('\n'.join(map(str,ans)))

        



'''
根付き木にする。
後ろのクエリからやって、
色の確定した経路を圧縮していく。
UnionFind的な発想だけど計算量解析できてない。


'''