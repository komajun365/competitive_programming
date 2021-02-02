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

# 二分木
import bisect

n,m = map(int,input().split())
a = list(map(int,input().split()))

point = [0] * n
ans = [0] * m
for i,val in enumerate(a):
    ind = bisect.bisect_left(point,val*-1)
    if(ind < n):
        ans[i] = ind+1
        point[ind] = -val-1
    else:
        ans[i] = -1

print('\n'.join(map(str,ans)))
