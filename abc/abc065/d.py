import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n = int(input())
xs = []
ys = []
for i in range(n):
    x,y = map(int, input().split())
    xs.append([x,i])
    ys.append([y,i])

xs.sort()
ys.sort()

edges = []
for tmp in [xs,ys]:
    for i in range(n-1):
        tmp_0 = tmp[i]
        tmp_1 = tmp[i+1]
        edges.append([ tmp_1[0] - tmp_0[0], tmp_1[1], tmp_0[1] ])

edges.sort()

ans = 0
uf = list(range(n))
remains = set(range(1,n))

def get_root(a):
    tmp = uf[a]
    if(a == tmp):
        return a
    uf[a] = get_root(tmp)
    if((uf[a] == 0)& (a in remains) ):
        remains.remove(a)
    return uf[a]

def update(a, next):
    if(a != uf[a]):
        update(uf[a], next)
    uf[a] = next

# print(edges)

for edge in edges:
    cost, a, b = edge
    root_a = get_root(a)
    root_b = get_root(b)
    min_ = min(root_a, root_b)
    if( root_a != root_b):
        update(a, min_)
        update(b, min_)
        ans += cost
        # print(uf)
        # print(ans)
    if(min_ == 0):
        rem_temp = remains.copy()
        for remain in rem_temp:
            get_root(remain)

        if(len(remains) == 0):
            print(ans)
            exit()
