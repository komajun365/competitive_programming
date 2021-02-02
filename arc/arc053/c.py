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

n,*ab = map(int,read().split())
p = []
m = []
it = iter(ab)
for a,b, in zip(it,it):
    if(a-b < 0):
        m.append([a,b])
    else:
        p.append([a,b])

m.sort(key=lambda x: x[0])
p.sort(key=lambda x: -1 * x[1])

mp = m+p
ans = 0
now = 0
for a,b in mp:
    ans = max(ans, now+a)
    now += a-b
print(ans)
