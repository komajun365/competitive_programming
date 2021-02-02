# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import bisect

n,w,c = map(int,readline().split())
lrp = [list(map(int, i.split())) for i in readlines()]

lrp = sorted(lrp, key=lambda x: x[1])
left = [0] * (n+1)
left_cost = [0] * (n+1)
for i,(l,r,p) in enumerate(lrp,1):
    left[i] = r
    left_cost[i] = left_cost[i-1] + p

lrp = sorted(lrp)
right = [w] * (n+1)
right_cost = [0] * (n+1)
for i,(l,r,p) in enumerate(lrp[::-1],2):
    right[-i] = l
    right_cost[-i] = right_cost[-i+1] + p

all_cost = right_cost[0]

search = [0] + [r for l,r,p in lrp]

ans = all_cost
for x in search:
    tmp = all_cost
    ind = bisect.bisect_right(left,x)
    tmp -= left_cost[ind-1]
    if(x+c > w):
        continue
    ind = bisect.bisect_left(right,x+c)
    tmp -= right_cost[ind]
    ans = min(ans,tmp)

print(ans)

# print(sorted(lrp, key=lambda x: x[1]))

# points = []
# for l,r,p in lrp:
#     points.append((l,p))
#     points.append((r,-1*p))
#
# points.sort()
# pp = [i for i,j in points]
# pc = [j for i,j in points]
#
# print(points)
