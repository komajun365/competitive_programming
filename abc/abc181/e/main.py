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

import bisect

n,m = map(int,input().split())
h = list(map(int,input().split()))
w = list(map(int,input().split()))

h.sort()
cs_l = [0] * (n+3)
cs_r = [0] * (n+3)

tmp = 0
for i in range(1,n,2):
    tmp += h[i]-h[i-1]
    cs_l[i] = tmp

tmp = 0
for i in range(n-2,0,-2):
    tmp += h[i+1]-h[i]
    cs_r[i] = tmp

ans = 10**16
for wi in w:
    i = bisect.bisect_left(h,wi)
    tmp = 0
    if(i%2==0):
        tmp = cs_l[i-1]
        tmp += cs_r[i+1]
        tmp += abs(h[i] - wi)
    else:
        tmp = cs_l[i-2]
        tmp += cs_r[i]
        tmp += abs(h[i-1] - wi)
    ans = min(ans,tmp)
print(ans)

