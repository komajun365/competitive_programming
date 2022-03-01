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
base = (1<<20) - 1
def dijkstra(links, start, n):
    inf = 10**10
    d = [dict() for _ in range(n)]
    done = [inf] * n
    d[start][0] = 0
    done[start] = 0
    hq = []
    for x in links[start]:
        c = x >> 20
        i = x & base
        heapq.heappush(hq, (1<<40) + (c<<20) + i)
    while hq:
        x = heapq.heappop(hq)
        cost = x>>40
        cnt = (x>>20) & base
        i = x & base
        if done[i] <= cnt:
            continue
        done[i] = cnt
        d[i][cnt] = cost
        for tmp in links[i]:
            c = tmp >> 20
            j = tmp & base
            if done[j] <= cnt + c:
                continue
            cost_next = cost + 1
            if c == 1:
                cost_next += cnt
            heapq.heappush(hq, (cost_next<<40) + ((cnt+c)<<20) + j)
    return d

n,m,*cab = map(int,read().split())


links = [[] for _ in range(n)]
it = iter(cab)
for c,a,b in zip(it,it,it):
    links[a].append((c << 20) + b)
    links[b].append((c << 20) + a)

d = dijkstra(links, 0, n)

ans = []
for i in range(n):
    tmp = 10**10
    for j in d[i].values():
        tmp = min(tmp, j)
    ans.append(tmp)
print('\n'.join(map(str,ans)))
