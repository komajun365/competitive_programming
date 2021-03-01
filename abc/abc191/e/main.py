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

import heapq
def dijkstra(links, start, n):
    inf = 10**10
    d = [inf] * (n)
    hq = []
    for cost,i in links[start]:
        heapq.heappush(hq, cost*inf + i)
    while(hq):
        num = heapq.heappop(hq)
        cost = num//inf
        i = num%inf
        if( d[i] != inf):
            continue
        d[i] = cost
        if i == start:
            return d
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, inf*(cost+cost_next)+j )
    return d

import sys
read = sys.stdin.buffer.read
n,m,*abc = map(int,read().split())

inf = 10**10
ans = [inf] * n
links = [[] for _ in range(n)]
it = iter(abc)
for a,b,c in zip(it,it,it):
    a -= 1
    b -= 1
    if a==b:
        ans[a] = min(ans[a],c)
    else:
        links[a].append([c,b])

for i in range(n):
    d = dijkstra(links, i, n)
    ans[i] = min(ans[i], d[i])

for i in range(n):
    if ans[i] == inf:
        ans[i] = -1

print('\n'.join(map(str,ans)))




