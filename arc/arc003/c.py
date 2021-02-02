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

from heapq import heappop,heappush

n,m = map(int,input().split())
c = [input() for _ in range(n)]

inf = 10**10

cost = [[inf] * (m+2) for _ in range(n+2)]
dp = [[inf] * (m+2) for _ in range(n+2)]
done = [[False]* (m+2) for _ in range(n+2)]

start = [0,0]
goal = [0,0]
for i in range(n):
    for j in range(m):
        if(c[i][j] == 's'):
            cost[i+1][j+1] = inf - 1
            start = [i+1,j+1]
        elif(c[i][j] == 'g'):
            cost[i+1][j+1] = 0
            dp[i+1][j+1] = inf
            done[i+1][j+1] = True
            goal = [i+1,j+1]
        elif(c[i][j] != '#'):
            cost[i+1][j+1] = int(c[i][j])

hq = [(inf*-1,goal)]
while(hq):
    ci,xy = heappop(hq)
    ci *= -1
    x,y = xy
    for xj,yj in zip([-1,1,0,0,],[0,0,-1,1]):
        xj += x
        yj += y
        if(done[xj][yj])|(cost[xj][yj]==inf):
            continue
        dp[xj][yj] = min(cost[xj][yj] , ci*0.99)
        done[xj][yj] = True
        heappush(hq,( -1 * dp[xj][yj],[xj,yj]))

x,y = start
if(done[x][y]):
    print(dp[x][y])
else:
    print(-1)


'''
ゴールからダイクストラかな

'''
