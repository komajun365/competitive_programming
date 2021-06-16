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

# dijkstra
import heapq
def dijkstra(links, start, n):
    inf = 10**10
    d = [inf] * (n)
    d[start] = 0
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
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, inf*(cost+cost_next)+j )
    return d

n,m,*abc = map(int,read().split())

links = [[] for _ in range(n)]
it = iter(abc)
for a,b,c in zip(it,it,it):
    a -= 1
    b -= 1
    links[a].append([c,b])
    links[b].append([c,a])

d0 = dijkstra(links, 0, n)
d1 = dijkstra(links, n-1, n)

ans = []
for i in range(n):
    ans.append(str(d0[i] + d1[i]))

print('\n'.join(ans))