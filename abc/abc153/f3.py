import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline
# 二分木
import bisect


n,d,a = map(int,input().split())
xh = [list(map(int, input().split())) for _ in range(n)]

xh.sort()
x = [ tmp[0] for tmp in xh]
damage = [0] * (n+1)

ans = 0
for i in range(n):
    damage[i+1] += damage[i]
    if( damage[i+1] >= xh[i][1] ):
        continue
    atk_num = (xh[i][1] - damage[i+1] - 1)//a +1
    ans += atk_num
    damage[i+1] += atk_num * a
    right = bisect.bisect_right(x, xh[i][0] + 2*d)
    if( right < n):
        damage[right+1] -= atk_num * a

print(ans)
