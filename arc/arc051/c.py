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

from heapq import heappop,heappush

N,A,B = map(int,input().split())
a = list(map(int,input().split()))
mod = 10**9+7

if(A==1):
    a.sort()
    print('\n'.join(map(str,a)))
    exit()

hq = []
ans = []
for ai in a:
    heappush(hq,ai)

while(B>0):
    if(not hq):
        break
    tmp = heappop(hq)
    tmp *= A
    if(tmp <= 10**9):
        heappush(hq,tmp)
    else:
        ans.append(tmp)
    B -= 1

for hq_i in hq:
    ans.append(hq_i)

ans.sort()
for i in range(B%N):
    ans[i] *= A

ans.sort()
for i in range(N):
    ans[i] %= mod
    ans[i] *= pow(A,B//N,mod)
    ans[i] %= mod

print('\n'.join(map(str,ans)))
