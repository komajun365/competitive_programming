# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f


import sys
input = sys.stdin.readline
from collections import deque
import bisect

n = int(input())
a = list(map(int,input().split()))

links = [[] for _ in range(n+1)]
for _ in range(n-1):
    v,w = map(int, input().split())
    links[v].append(w)
    links[w].append(v)

inf = 10**10
lis = [inf] * n
inf_ind = 0
parent = [-1]*(n+1)
operate = [0] * (n+1)
ans = [-1]*(n+1)
d = deque()
d.append(1)
while(d):
    now = d.popleft()
    if(operate[now]==0):
        p = parent[now]
        if(p!=-1):
            d.appendleft(now)
        for child in links[now]:
            if(child != p):
                parent[child] = now
                d.appendleft(child)

        a_now = a[now-1]
        ind = bisect.bisect_left(lis,a_now)
        operate[now] = (ind,lis[ind],a_now)
        lis[ind] = a_now
        if(inf_ind == ind):
            inf_ind += 1
        ans[now] = inf_ind
    else:
        ind,before,after = operate[now]
        lis[ind] = before
        if(before == inf):
            inf_ind -= 1
    # print(lis)

for i in ans[1:]:
    print(i)
