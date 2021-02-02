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
from collections import deque
import itertools

n,m = map(int,readline().split())
data = list(map(int,read().split()))

links = [[] for _ in range(n+1)]
it = iter(data[:m*2])
for u,v in zip(it,it):
    links[u].append(v)
    links[v].append(u)
s = data[m*2]
k = data[m*2+1]
t = data[m*2+2:]

# t間の距離を計算
st = [-1] * (k)
links2 = [{} for _ in range(k)]
for ind,i in enumerate(t):
    d = [-1] * (n+1)
    d[i] = 0
    dq = deque()
    dq.append((i,0))
    while(dq):
        now,dif = dq.popleft()
        for j in links[now]:
            if(d[j] == -1):
                d[j] = dif + 1
                dq.append((j,dif+1))

    for ind_j,j in enumerate(t):
        if(i!=j):
            links2[ind][ind_j] = d[j]
    st[ind] = d[s]

inf = 10**10
dp = [[inf] * (1<<k) for _ in range(k)]
for i,dif in enumerate(st):
    dp[i][1<<i] = dif

# skips = set()
# for i in range(k):
#     skips.add(1<<i)


for i in range(1,(1<<k)):
    # if(i in skips):
    #     continue

    for j in range(k):
        if((i>>j)&1):
            for l in range(k):
                if((i>>l)&1)&(j!=l):
                    dp[j][i] = min(dp[j][i], dp[l][i^(1<<j)] + links2[j][l])


ans = inf
for i in range(k):
    ans = min(ans,dp[i][-1])
print(ans)
