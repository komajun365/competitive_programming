# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]

inf = 10**10
cost1 = [[inf] * w for _ in range(h)]
cost2 = [[inf] * w for _ in range(h)]
cost3 = [[inf] * w for _ in range(h)]

cost1[-1][0] = 0
cost2[-1][-1] = 0
cost3[0][-1] = 0

for ct in [cost1,cost2,cost3]:
    remain = set()
    for i in range(h):
        for j in range(w):
            remain.add((i,j))
    for _ in range(h*w):
        cand = (inf,(-1,-1))
        for (i,j) in remain:
            if(cand[0] > ct[i][j]):
                cand = (ct[i][j],(i,j))
        i,j = cand[1]
        remain.remove((i,j))
        for x,y in zip([0,0,1,-1],[1,-1,0,0]):
            x += j
            y += i
            if(0<=x<w)&(0<=y<h):
                ct[y][x] = min(ct[y][x], ct[i][j] + a[y][x])

ans = inf
for i in range(h):
    for j in range(w):
        tmp = 0
        for ct in [cost1,cost2,cost3]:
            tmp += ct[i][j]
        tmp -= a[i][j]*2
        ans = min(ans,tmp)

print(ans)
