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

import sys
read = sys.stdin.buffer.read

n,q,*data = map(int,read().split())

xy = data[:2*n]
q = data[2*n:]

inf = 10**10
xy_pl = inf
xy_pr = -1*inf
xy_ml = inf
xy_mr = -1*inf

it = iter(xy)
for x,y in zip(it,it):
    xy_pl = min(xy_pl, x+y)
    xy_pr = max(xy_pr, x+y)
    xy_ml = min(xy_ml, x-y)
    xy_mr = max(xy_mr, x-y)

ans = []
for qi in q:
    x0,y0 = xy[qi*2-2: qi*2]
    xy_p = x0+y0
    xy_m = x0-y0
    tmp = max(abs(xy_pl-xy_p), abs(xy_pr-xy_p),
              abs(xy_ml-xy_m), abs(xy_mr-xy_m))
    ans.append(tmp)

print('\n'.join(map(str,ans)))