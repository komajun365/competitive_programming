# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
mod = 10**9+7

# dijkstra
import heapq
def dijkstra(links, start,goal, n):
    inf = 10**20
    d = [inf] * (n)
    cnt = [0] * n
    d[start] = 0
    cnt[start] = 1
    # befs = [[] for _ in range(n+1)]
    hq = []
    for i in links[start]:
        heapq.heappush(hq, (i[0],i[1],start))
    while(hq):
        cost,i,bef = heapq.heappop(hq)
        if(cost > d[goal]):
            return d,cnt
        if( d[i] != inf):
            if(d[i] == cost):
                cnt[i] += cnt[bef]
                cnt[i] %= mod
                # befs[i].append(bef)
            continue
        d[i] = cost
        cnt[i] += cnt[bef]
        # befs[i].append(bef)
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, (cost+cost_next, j,i))
    return d,cnt

n,m = map(int,readline().split())
s,t = map(int,readline().split())
uvd = list(map(int,read().split()))

links = [[] for _ in range(n+1)]
it = iter(uvd)
for u,v,d in zip(it,it,it):
    links[u].append((d*2,v))
    links[v].append((d*2,u))

d_st,cnt_st = dijkstra(links, s,t, n+1)
d_ts,cnt_ts = dijkstra(links, t,s, n+1)

half = d_st[t]//2

collision = 0
for i in range(1,n+1):
    if(d_st[i] == half)&(d_ts[i]==half):
        tmp = (cnt_st[i] * cnt_ts[i])%mod
        collision += (tmp**2)%mod
        collision %= mod

it = iter(uvd)
for u,v,d in zip(it,it,it):
    for p1,p2 in zip([u,v],[v,u]):
        if(d_st[p1] < half < d_st[p2])&(d_ts[p1] > half > d_ts[p2])& \
            (d_st[p2] - d_st[p1] == d*2)&(d_ts[p1] - d_ts[p2] == d*2) :
                tmp = (cnt_st[p1] * cnt_ts[p2])%mod
                collision += (tmp**2)%mod
                collision %= mod

ans = (cnt_st[t]**2 - collision)%mod
print(ans)

print(cnt_st[t])
print(d_st)
print(cnt_st)
print(d_ts)
print(cnt_ts)

# it = iter(uvd)
# for u,v,d in zip(it,it,it):



'''
出会う可能性のある場所と、そこまでの到達方法の数をカウントしたい。

1回ダイクストラ
→　時間を把握


'''
