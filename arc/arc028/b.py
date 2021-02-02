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

n,k = map(int,input().split())
x = list(map(int,input().split()))

hq = []
ans = []
for i,xi in enumerate(x,1):
    if(i <= k):
        heappush(hq,(-xi,i))
    if(i==k):
        ans.append(hq[0][1])
    elif(i > k):
        if(hq[0][0] > -xi):
            ans.append(hq[0][1])
        else:
            heappop(hq)
            heappush(hq,(-xi,i))
            ans.append(hq[0][1])

print('\n'.join(map(str,ans)))


