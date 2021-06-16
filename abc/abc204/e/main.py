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

import heapq
def dijkstra(links, start, n):
    inf = 10**15
    base = (1<<20) -1
    d = [inf] * (n)
    d[start] = 0
    hq = []
    for i in links[start]:
        bi,ci,di,wait = edge[i]
        cost = ci + wait + di//(wait+1)
        heapq.heappush(hq, (cost<<20) + bi)
    while(hq):
        num = heapq.heappop(hq)
        cost = num >> 20
        i = num & base
        if( d[i] != inf):
            continue
        d[i] = cost
        for j in links[i]:
            bj,cj,dj,wait = edge[j]
            if cost <= wait:
                cost_next = cj + wait + dj//(wait+1)
            else:
                cost_next = cost + cj + dj//(cost+1)
            if(d[bj] == inf):
                heapq.heappush(hq, (cost_next<<20)+bj )
    return d

def search(di):
    left,right = 0, di-1
    num = [di,di]
    while right - left > 2:
        l1 = (left*2+right)//3
        l2 = (left+right*2)//3
        n1 = l1 + di//(l1+1)
        n2 = l2 + di//(l2+1)
        if n1 == n2:
            left,right = l1,l2
            num = [n1,n2]
        elif n1 < n2:
            right = l2
            num[1] = n2
        else:
            left = l1
            num[0] = n1
    
    res = left
    n_min = num[0]
    for l1 in range(max(0,left-50),right+50):
        n1 = l1 + di//(l1+1)
        if n_min > n1:
            res = l1
            n_min = n1
    return res

n,m,*abcd = map(int,read().split())

links = [[] for _ in range(n)]
edge = []
for i in range(m):
    a,b,c,d = abcd[i*4:i*4+4]
    a -= 1
    b -= 1
    links[a].append(i*2)
    links[b].append(i*2+1)
    wait = search(d)
    edge.append([b,c,d,wait])
    edge.append([a,c,d,wait])

d = dijkstra(links, 0, n)
if d[-1] >= 10**15:
    print(-1)
else:
    print(d[-1])