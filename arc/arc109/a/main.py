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

a,b,x,y = map(int,input().split())
a -= 1
b -= 1

links = [[] for _ in range(200)]
for i in range(99):
    links[i].append((y,i+1))
    links[i+1].append((y,i))
    links[i+100].append((y,i+101))
    links[i+101].append((y,i+100))
 
for i in range(100):
    links[i].append((x,i+100))
    links[i+100].append((x,i))

for i in range(99):
    links[i+100].append((x,i+1))
    links[i+1].append((x,i+100))

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

d = dijkstra(links, a, 200)
print(d[100+b])