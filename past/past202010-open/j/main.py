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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n,m = map(int,readline().split())
x = list(map(int,readline().split()))
s = readline().split()[0]
abc = list(map(int,read().split()))

import heapq
def dijkstra(links, start, n):
    inf = 10**18
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

n2 = n + 4
links = [[] for _ in range(n2)]

it = iter(abc)
for a,b,c in zip(it,it,it):
    links[a].append((c,b))
    links[b].append((c,a))

for i,si in enumerate(s,1):
    if(si=='A'):
        links[i].append((x[0], n+2))
        links[i].append((x[1], n+3))
        links[n+1].append((0, i))
    elif(si=='B'):
        links[i].append((x[0], n+1))
        links[i].append((x[2], n+3))
        links[n+2].append((0, i))
    else:
        links[i].append((x[1], n+1))
        links[i].append((x[2], n+2))
        links[n+3].append((0, i))

d = dijkstra(links, 1, n2)
print(d[n])