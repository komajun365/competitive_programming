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

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

hq = []
for i,(ai,bi) in enumerate(zip(a,b)):
    if(bi > ai):
        heappush(hq,(bi*-1,i))
    elif(bi < ai):
        print(-1)
        exit()

ans = 0
while(hq):
    _,ind = heappop(hq)
    side = b[(ind-1)%n] + b[(ind+1)%n]
    if(b[ind] <= side):
        print(-1)
        exit()
    cand = b[ind]%side
    if( cand > a[ind]):
        ans += (b[ind] - cand)//side
        b[ind] = cand
        heappush(hq,(-1*cand,ind))
    else:
        if(cand == a[ind]%side):
            cand = a[ind]
            ans += (b[ind] - cand)//side
            b[ind] = cand
        else:
            print(-1)
            exit()

print(ans)
