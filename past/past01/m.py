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

n,m = map(int,readline().split())
data = list(map(int,read().split()))
it = iter(data[:2*n])
ab = [[a,b] for a,b in zip(it,it)]
it = iter(data[2*n:])
cd = [[c,d] for c,d in zip(it,it)]

ok = 0
ng = 100001
for i in range(100):
    mid = (ok+ng)/2
    mon = [b-a*mid  for a,b in ab]
    help = [b-a*mid  for a,b in cd]
    mon.sort(reverse=True)
    help.sort(reverse=True)
    mon[4] = max(mon[4],help[0])
    if( sum(mon[:5]) >=0 ):
        ok = mid
    else:
        ng = mid

print(ok)
