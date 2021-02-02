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

n = int(readline())
data = list(map(int,read().split()))

inf = 10**15
axis_p_max = -1 * inf
axis_p_min = inf
axis_m_max = -1 * inf
axis_m_min = inf

it = iter(data)
for x,y in zip(it,it):
    axis_p_max = max(axis_p_max, x+y)
    axis_p_min = min(axis_p_min, x+y)
    axis_m_max = max(axis_m_max, x-y)
    axis_m_min = min(axis_m_min, x-y)

ans = max(axis_p_max-axis_p_min, axis_m_max-axis_m_min)
print(ans)
