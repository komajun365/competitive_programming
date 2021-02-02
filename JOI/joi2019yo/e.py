# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討10分　実装20分 バグとり0分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int,readline().split())
a = list(map(int,readline().split()))
it = iter(list(map(int,read().split())))
lr = [0] * m
for i,(l,r) in enumerate(zip(it,it)):
    lr[i] = (l,r)

lr.sort()
b = list(range(1,n+2))
for l,r in lr:
    b[l] = max(b[l], r+1)

for i in range(1,n+1):
    b[i] = max(b[i],b[i-1])

cumsum = [0] * (n+1)
for i in range(1,n+1):
    cumsum[i] = cumsum[i-1]+a[i-1]

links = [[] for _ in range(n+2)]
for i in range(1,n+1):
    links[i].append((a[i-1],i+1))
    links[i].append((cumsum[b[i]-1] - cumsum[i]  , b[i]))

links[0].append((0,1))

# dijkstra
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

d = dijkstra(links,0,n+2)
print(cumsum[-1] - d[-1])


'''
ダイクストラ。
各木に対して、その木にイルミネーション付けた場合に、
次にイルミネーションがつけられる木（Bi）を調べておく。

番兵として木0と木n+1を追加しておく。　※木0はいらなかったかも
木iから木i+1への移動はコストAiである。
これは木iにイルミネーションを付けないことを表す。

次に木iにイルミネーションを付ける場合。
これは、木iから木Biへの移動に相当する。
このコストはsum[木i+1～木Bi-1]であらわせる。

この条件で、最小の移動コストを求め、すべてのイルミネーションの合計値との差分をとる。
'''
