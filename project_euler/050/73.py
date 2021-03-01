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

from collections import deque
ns = deque()
ns.append(1)
ds = deque()
ds.append(2)

ans = 0
n,d = 1,3
while(ds):
    n2 = ns[0]
    d2 = ds[0]
    if d + d2 <= 12000:
        ns.appendleft(n + n2)
        ds.appendleft(d + d2)
    else:
        n = ns.popleft()
        d = ds.popleft()
        ans += 1

print(ans-1)





'''
既約分数を並べて、分子と分母を足すと良い感じの分数が作られることが知られています。

1/3 と 1/2 の間に　(1+1)/(3+2)がある、みたいな

'''