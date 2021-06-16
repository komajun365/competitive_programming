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


import sys
read = sys.stdin.buffer.read

r,c,*data = map(int,read().split())

a = data[:r*(c-1)]
b = data[r*(c-1):]

n = r*c
n2 = r*c*2
links = [[] for _ in range(n2)]

for i in range(r):
    for j in range(c-1):
        links[i*c+j].append([a[i*(c-1)+j], i*c+j+1])
        links[i*c+j+1].append([a[i*(c-1)+j], i*c+j])

for i in range(r-1):
    for j in range(c):
        links[i*c+j].append([b[i*c+j], (i+1)*c+j])
        links[(i+1)*c+j+n].append([1, i*c+j+n])

for i in range(r):
    for j in range(c):
        links[i*c+j].append([1, i*c+j+n])
        links[i*c+j+n].append([0, i*c+j])

d = dijkstra(links,0,n2)
ans = d[r*c-1]
print(ans)

