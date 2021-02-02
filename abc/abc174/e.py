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

n,k = map(int,input().split())
a = list(map(int,input().split()))

ok = max(a)
ng = 0
for _ in range(50):
    mid = (ok+ng)//2
    if(mid==0):
        print(1)
        exit()
    cnt = 0
    for ai in a:
        cnt += (ai-1)//mid
    if(cnt <= k):
        ok = mid
    else:
        ng = mid

print(ok)
