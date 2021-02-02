# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討7分　実装38分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import heapq

inf = 10**10

n,m,x = map(int, readline().split())
data = list(map(int, read().split()))
t = tuple(data[:n])

links = [[] for _ in range(n+1)]
it = iter(data[n:])
for a,b,d in zip(it,it,it):
    links[a].append((d,b))
    links[b].append((d,a))

dp = [[inf] * (2*x+1) for _ in range(n+1)]

hq = [(0,1,0)]
while(hq):
    cost,i,mi = heapq.heappop(hq)
    if(dp[i][mi] != inf):
        continue
    dp[i][mi] = cost
    if(i==n):
        print(cost)
        exit()
    ti = t[i-1]
    for cost_j, j in links[i]:
        tj = t[j-1]
        if(ti!=tj)&(ti+tj==2):
            if(cost_j>=x)&(dp[j][0]==inf):
                heapq.heappush(hq,(cost+cost_j,j,0))
            continue
        if(ti==1)&(tj==0):
            if(mi-cost_j<=0)&(dp[j][0]==inf):
                heapq.heappush(hq,(cost+cost_j,j,0))
            continue
        if(ti==1)&(tj==2):
            if(mi+cost_j>=0)&(dp[j][0]==inf):
                heapq.heappush(hq,(cost+cost_j,j,0))
            continue
        if(ti==tj)&(ti!=1):
            mj = 0
        elif(ti==1)&(tj==1):
            if(mi < 0):
                mj = min(0, mi+cost_j)
            elif(mi>0):
                mj = max(0, mi-cost_j)
            else:
                mj = 0
        else:
            mj = (ti-1)*max(0,x-cost_j)
        if(dp[j][mj]==inf):
            heapq.heappush(hq,(cost+cost_j,j,mj))



'''
[0,2][2,0]
[1,0]
[1,2]

[0,0][2,2]
[1,1]
[0,1][2,1]

'''
