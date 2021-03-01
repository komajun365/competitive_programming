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

beauty = [a[0]]
base = [a[0]]

for ai in a[1:]:
    for i in range(len(base)):
        base[i] += ai
        beauty.append(base[i])
    beauty.append(ai)
    base.append(ai)

ans = 0
for bi in range(41,-1,-1):
    cand = []
    for i in beauty:
        if((i>>bi)&1):
            cand.append(i)
    if(len(cand) >= k):
        ans += 1<<bi
        beauty = cand

print(ans)
