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

ans = []
it = iter(data)
for a,b in zip(it,it):
    if(a > b):
        a,b = b,a
    ab = a*b
    ok = 0
    ng = b*2
    while(ng-ok > 1):
        mid = (ok+ng)//2
        x = (mid//2) * ((mid+1)//2)
        if( ab > x):
            ok = mid
        else:
            ng = mid
    ans.append(max(0,ok-2*a) + 2*a-2)

print('\n'.join(map(str,ans)))
