# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討15分　実装12分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,c = map(int,readline().split())
it = iter(map(int,read().split()))

sum_d = 0
links = [[] for _ in range(n+1)]
for a,b,d in zip(it,it,it):
    links[a].append((d,b))
    links[b].append((d,a))
    sum_d += d

import heapq
def dijkstra(links, start, n):
    inf = 10**10
    d = [inf] * (n)
    d[start] = 0
    hq = []
    for i in links[start]:
        heapq.heappush(hq, i)
    while(hq):
        cost,i = heapq.heappop(hq)
        if( d[i] != inf):
            continue
        d[i] = cost
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, (cost+cost_next, j))
    return d

d = dijkstra(links, 1, n+1)
d = list( (x,i) for i,x in enumerate(d[2:],2 ) )
d.sort()

ans = sum_d
del_d = 0
remain = set(range(2,n+1))
for x, i in d:
    for cost,j in links[i]:
        if(not j in remain):
            del_d += cost
    remain.remove(i)

    tmp = sum_d - del_d + c*x
    ans = min(ans, tmp)

print(ans)


'''
方針
ダイクストラで広場１からの距離を計算していく。
広場iを広場1からの距離でソートし、
近い広場から地下道を作っていったとき、
新たに撤去する道を確認し、そこでのコストを計算する。

ダイクストラがO(N+MlogM)
ソートがO(NlogN)
コストの確認がO(M)で計算できる。
全体の計算量はO(NlogN+MlogM)

'''
