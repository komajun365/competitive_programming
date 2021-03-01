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

## dijkstraの時間測りたいだけ

import sys
read = sys.stdin.buffer.read

import heapq
def dijkstra(links, start, n):
    inf = 10**15
    base = (1<<20) - 1
    d = [inf] * n
    cnt = [0] * n
    d[start] = 0
    cnt[start] = 1
    hq = []
    for cost,i in links[start]:
        heapq.heappush(hq, (cost << 20)+ i)
        d[i] = cost
        cnt[i] = 1
    while(hq):
        num = heapq.heappop(hq)
        cost = num >> 20
        i = num & base
        if( d[i] < cost):
            continue
        for cost_next, j in links[i]:
            cost_next += cost
            if d[j] < cost_next:
                continue
            elif d[j] == cost_next:
                cnt[j] += cnt[i]
                cnt[j] %= mod
            else:
                d[j] = cost_next
                cnt[j] = cnt[i]
                heapq.heappush(hq, (cost_next << 20)+ j)
    return d,cnt

n,m,s,t,*uvd = map(int,read().split())
mod = 10**9 + 7
s -= 1
t -= 1

links = [[] for _ in range(n)]
it = iter(uvd)
for u,v,d in zip(it,it,it):
    u -= 1
    v -= 1
    links[u].append([d,v])
    links[v].append([d,u])

ds,cnt_s = dijkstra(links,s,n)
time = ds[t]
dt,cnt_t = dijkstra(links,t,n)

ans = cnt_s[t]**2 % mod

for i in range(n):
    if ds[i] == dt[i] == time//2:
        ans -= (cnt_s[i] * cnt_t[i] % mod) ** 2
        ans %= mod
    
it = iter(uvd)
for u,v,d in zip(it,it,it):
    u -= 1
    v -= 1
    if ds[u] + dt[v] + d == time and ds[u]*2 < time and dt[v]*2 < time:
        ans -= (cnt_s[u] * cnt_t[v] % mod) ** 2
        ans %= mod
    if dt[u] + ds[v] + d == time and dt[u]*2 < time and ds[v]*2 < time:
        ans -= (cnt_t[u] * cnt_s[v] % mod) ** 2
        ans %= mod

print(ans)

# print(ds)
# print(cnt_s)
# print(dt)
# print(cnt_t)